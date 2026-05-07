# Komunikační modul pro bezpilotní letoun

**Adam Mikulič** — Maturitní projekt, Gymnázium Havlíčkův Brod 2026

---

## Abstrakt

Evropská legislativa omezuje vysílací výkon pro rádiové řízení, což drasticky snižuje bezpečný dosah bezpilotních letounů (UAV) v členitém terénu. Cílem této práce je vyvinout modul, který toto fyzické omezení dosahu spolehlivě překoná. Problém je řešen návrhem a konstrukcí vzdušného komunikačního modulu (relay node) fungujícího jako most pro vysokorychlostní protokol CRSF. Řešení využívá mikrokontrolér ESP32 s optimalizací na dvě jádra a vlastní převodní desku pro half-duplexní komunikaci. Během reálných letových testů systém prokazatelně a stabilně zdvojnásobil efektivní dosah řídicího spojení na vzdálenost 2 km, a to zcela bez znatelného nárůstu latence či výpadků. Projekt přináší plně funkční, kompaktní a dostupné řešení pro bezpečný provoz UAV na delší vzdálenosti, které respektuje legislativní limity a přidává inovativní diagnostické webové rozhraní.

---

### 1. Úvod

Evropská legislativa přísně omezuje maximální povolený vysílací výkon pro rádiové řízení (limity CE LBT v pásmech 2.4 GHz a 868 MHz). Toto omezení snižuje efektivní a bezpečný dosah bezpilotních letounů, a to zejména v členitém terénu, kde dochází ke ztrátě přímé viditelnosti mezi pilotem a strojem.

Cílem tohoto projektu je vyvinout a otestovat spolehlivý komunikační modul, který fyzická omezení dosahu překoná. Aby bylo řešení v praxi použitelné, musí fungovat jako most pro řídicí protokol CRSF. Je nutné, aby systém zpracovával data s nízkou ztrátou paketů, nevnášel do řídicí smyčky podstatnou latenci a zároveň umožňoval snadný monitoring stavu spojení. Zařízení také musí být kompaktní, aby jej bylo možné snadno integrovat do bezpilotního letounu.

Běžné přístupy k řešení omezeného dosahu zahrnují nelegální plošné zvyšování vysílacího výkonu nebo použití směrových antén, což vyžaduje přesné míření a omezuje mobilitu pilota. Další možností je nasazení vzdušných retranslačních stanic (repeaterů). Tyto systémy, které plně prokázaly svou efektivitu například při nasazení UAV v konfliktu na Ukrajině, překonávají překážky v terénu tím, že přenášejí signál z vyvýšeného bodu.

Navržené řešení představuje vlastní hardwarový a softwarový návrh komunikačního modulu postaveného na mikrokontroléru ESP32. Systém izoluje zpracování rádiového signálu na jedno jádro procesoru, čímž zajišťuje okamžité přeposílání přijatých dat do výkonného TX modulu přes vlastní převodní PCB desku. Druhé jádro mikrokontroléru se mezitím stará o obsluhu WiFi přístupového bodu.

Výsledný komunikační modul prokazatelně zdvojnásobuje efektivní dosah komunikace při zachování neznatelné latence přeposílací smyčky. Systém nevykazuje žádnou ztrátu funkčnosti spojení a jako přidanou hodnotu nabízí integrovaný webový dashboard pro realtime diagnostiku a nastavení.

---

### 2. Teoretický úvod a analýza

### 2.1 Komunikační protokol CRSF a ExpressLRS

Základním předpokladem pro spolehlivé ovládání bezpilotních letounů (UAV) je robustní rádiové spojení s nízkou latencí. V současné době je pro tyto účely hojně využíván open-source systém ExpressLRS (ELRS). Ten pro komunikaci mezi svými hardwarovými moduly a řídicí elektronikou letounu využívá sériový protokol CRSF.

Komunikace přes CRSF probíhá prostřednictvím sběrnice UART vysokou rychlostí, typicky 400 000 až 420 000 baudů. V případě řídicích povelů (tzv. RC kanálů) je přenos realizován pomocí datových rámců o pevné délce 26 bajtů. Každý takový rámec začíná synchronizačním bajtem (např. 0xEE pro rámce směřující do vysílacího modulu), následuje informace o délce, identifikátor typu dat (0x16 pro kanály kniplů) a 22 bajtů samotného užitečného zatížení (payload).

Vysoká efektivita protokolu spočívá v bitovém balení: všech 16 dostupných RC kanálů je reprezentováno 11bitovými hodnotami (v rozsahu 0 až 2047), které jsou sekvenčně sbaleny do zmíněných 22 bajtů. Rámec je následně zakončen kontrolním součtem CRC-8 (polynom 0xD5), který zajišťuje detekci chyb při přenosu.

> Obrázek 1 — Vizualizace struktury CRSF protokolu

### 2.2 Topologie komunikačního modulu

Běžné rádiové spojení probíhá přímo mezi vysílačem pilota a přijímačem v letounu. Tento projekt do architektury vkládá mezistupeň v podobě retranslačního modulu, který funguje jako transparentní most. Z hlediska datového toku systém funguje v následujících krocích:

1. **Příjem povelů:** Vstupní přijímač (ELRS RX) na relay nodu zachytí rádiový signál ze vzdáleného vysílače pilota a dekóduje jej na standardní CRSF rámce. Tyto rámce jsou odesílány přes UART spojení do mikrokontroléru.
2. **Zpracování (ESP32):** Mikrokontrolér zachytí příchozí data. Ačkoliv může data modifikovat (např. aplikovat softwarový omezovač výstupu na kanálu plynu), jeho primárním úkolem je rámce okamžitě znovu zabalit a připravit k odeslání.
3. **Přeposlání:** Zpracovaná data jsou odeslána přes druhou sériovou linku (400 kbaud) do výkonného vysílacího modulu (ELRS TX), který signál vysílá dál k cílovému dronu.
4. **Telemetrie:** Systém funguje obousměrně. Pokud přijímač v dronu odešle telemetrická data (např. statistiky o kvalitě linku – RSSI a LQ), vysílací modul na relay nodu je přijme a předá do mikrokontroléru ke zpracování.

> Obrázek 2 — Vizualizace provedení
---

### 3. Návrh a implementace hardwaru

Cílem hardwarového návrhu bylo vytvořit spolehlivý, kompaktní a energeticky nezávislý systém, který dokáže plynule propojovat dva oddělené rádiové moduly. Systém se skládá ze tří hlavních bloků: řídicího mikrokontroléru, rádiové soustavy a obvodů pro přizpůsobení logických úrovní a napájení.

### 3.1 Výběr mikrokontroléru a rádiových modulů

Jako výpočetní srdce celého modulu byl zvolen mikrokontrolér ESP32 (konkrétně verze WROOM-32). Jeho hlavním benefitem pro tento projekt je přítomnost 3 UART rozhraní, dvou nezávislých procesorových jader a integrovaný WiFi modul.

Rádiová vrstva je tvořena dvěma moduly ekosystému ExpressLRS:

- **Vstupní přijímač (ELRS RX):** Přijímá řídicí signál od pilota. K vývoji byl využit standardní přijímač v pásmu 2.4 GHz HGLRC ELRS 2.4G.
- **Výstupní vysílač (ELRS TX):** Zajišťuje vysílání signálu k bezpilotnímu letounu. Zvolen byl modul Emax Aeris Link Nano pracující v pásmu 900 MHz.

Využití odlišných frekvenčních pásem pro linku pilot–relay (2.4 GHz) a relay–dron (900 MHz) bylo zvoleno záměrně, aby se eliminovalo riziko vzájemného zarušení dvou výkonných vysílačů v těsné blízkosti.

### 3.2 Architektura napájení

Stabilní dodávka elektrické energie je pro spolehlivost rádiového spojení naprosto kritická. Výkonné vysílací moduly (s vysílacím výkonem nad 250 mW až 1 W) mohou ve špičkách odebírat proud blížící se hodnotě 2 A. Napájení takového modulu přímo z USB portu nebo 5V pinu mikrokontroléru ESP32 by vedlo k podpětí (brownoutu), neustálým restartům a ztrátě spojení.

Z tohoto důvodu byl navržen dedikovaný napájecí řetězec:

- Celý uzel je napájen z externí dvoučlánkové lithium–polymerové baterie (2S LiPo) o jmenovitém napětí 7,4 V.
- Vysílací TX modul je napájen napřímo z této baterie přes JST 2-pin konektor, což mu poskytuje dostatečný proudový odběr bez výkonových špiček omezujících zbytek elektroniky.
- Mikrokontrolér ESP32 a vstupní přijímač jsou napájeny přes dedikovaný step-down (buck) měnič, který efektivně snižuje napětí baterie na bezpečnou úroveň 5 V vhodnou pro vestavěný regulátor ESP32.

> Obrázek 3 — Foto použitého step-down měniče

### 3.3 Návrh převodní desky plošných spojů

Největší hardwarovou výzvou projektu byla rozdílná koncepce sériové komunikace mezi mikrokontrolérem a vysílacím modulem. Zatímco ESP32 využívá pro rozhraní UART standardní full-duplex zapojení (fyzicky oddělené vodiče pro vysílání TX a příjem RX), vysílací moduly formátu nano-bay komunikují po jediné sdílené half-duplexní datové lince.

Pro vyřešení této nekompatibility byla v softwaru KiCad navržena vlastní převodní deska plošných spojů. Jejím jádrem je integrovaný obvod SN74HC125DR, což je čtyřnásobný sběrnicový oddělovač (buffer) s třístavovými výstupy.

Zapojení využívá jedno z hradel tohoto obvodu k řízení toku dat:

- V režimu vysílání (TX) mikrokontrolér ESP32 přes pin GPIO 25 přivede na řídicí pin hradla (Output Enable) logickou nulu (LOW). Tím se hradlo otevře a propustí data na sdílenou linku směrem k modulu.
- Po dokončení odeslání rámce (přibližně po 680 µs) mikrokontrolér přepne pin GPIO 25 do stavu logické jedničky (HIGH). Výstup bufferu přejde do stavu vysoké impedance (odpojí se od linky), což umožní modulu odesílat zpětnou telemetrii přímo do přijímacího pinu (RX) na ESP32 bez rizika zkratu.

Toto vlastní hardwarové řešení zajišťuje plynulý obousměrný tok dat a umožňuje bezchybnou komunikaci v obou směrech rychlostí 400 kbaudů.

> Obrázek 4 — Foto vytištěné desky plošných spojů
---

### 4. Implementace firmwaru

### 4.1 Architektura zpracování (Dual-core approach)

Základním požadavkem na firmware komunikačního modulu byla garance naprosto plynulého toku dat. Běžné operace WiFi stacku, jako je navazování spojení nebo odesílání HTTP odpovědí, mohou do běhu programu vnést zpoždění (jitter) v řádech desítek milisekund.

Pro citlivý řídicí signál UAV, který je odesílán mnohokrát za vteřinu, by takové zpoždění znamenalo ztrátu plynulosti a možné výpadky spojení.

Tento problém byl vyřešen využitím operačního systému FreeRTOS, který umožňuje asymetrické rozdělení úloh mezi dvě fyzická jádra mikrokontroléru ESP32.

- **Core 1 (Rádiová úloha):** Na tomto jádře je spuštěna nekonečná smyčka s vysokou prioritou, která se stará výhradně o čtení sběrnic UART, parsování protokolu CRSF a časování half-duplexního přepínání.
- **Core 0 (Servisní úloha):** Zpracovává standardní smyčku programu, obsluhuje WiFi přístupový bod a jednoduchý webový server. Tím je zajištěno, že síťová komunikace nijak nezpomaluje rádiovou linku.

### 4.2 Zpracování dat a half-duplexní řízení

Rádiová smyčka na Core 1 běží v sub-milisekundových intervalech. Ve chvíli, kdy mikrokontrolér přijme od vstupního přijímače 26bajtový rámec s daty kniplů, provede jeho dekódování. Data jsou rozbalena, překontrolována a okamžitě znovu zabalena do nového CRSF paketu, doplněného o čerstvě vypočtený kontrolní součet CRC-8.

Při odesílání do výstupního modulu firmware striktně řídí stav převodního obvodu (bufferu SN74HC125DR). Před začátkem přenosu mikrokontrolér stáhne řídicí pin do logické nuly (LOW), čímž otevře datovou cestu. Následně odešle paket rychlostí 400 kbaudů. Přenos 26 bajtů při této rychlosti trvá přibližně 650 µs. Po uplynutí bezpečné prodlevy (680 µs) mikrokontrolér pin opět uzavře (HIGH), čímž převede linku do stavu vysoké impedance a uvolní sběrnici pro příjem zpětné telemetrie od modulu.

### 4.3 Servisní a diagnostické rozhraní

Ačkoliv modul během letu funguje zcela autonomně, pro snadné nastavení, troubleshooting a monitoring na ploše byl integrován lokální webový dashboard. Mikrokontrolér po zapnutí automaticky vytvoří vlastní WiFi přístupový bod (SoftAP), ke kterému se lze připojit běžným telefonem či notebookem bez nutnosti stahovat jakékoliv externí aplikace.

Toto rozhraní poskytuje přehled o stavu uzlu v reálném čase. Firmware neustále vyhodnocuje časové značky příchozích dat a na jejich základě určuje diagnostické stavy:

- **RC LOST:** Indikuje ztrátu spojení mezi pilotem a relay nodem (výpadek povelů delší než 100 ms).
- **MODULE OFF:** Upozorňuje na hardwarový problém s komunikací mezi ESP32 a vysílacím modulem.
- **DRONE LOST:** Detekuje absenci telemetrických dat od letounu (výpadek nad 1000 ms), což značí zalétnutí mimo dosah nebo ztrátu napájení palubního přijímače.

Kromě těchto stavů rozhraní zobrazuje živou telemetrii, zejména aktuální sílu signálu (RSSI) a kvalitu spojení (Link Quality). To zásadně usnadňuje předletovou přípravu a ověření funkčnosti celého řetězce ještě před vzletem.

---

### 5. Mechanická konstrukce a integrace

Po úspěšném návrhu elektroniky bylo nutné vyřešit bezpečné upevnění všech komponent a jeho integraci na vynášecí letoun. Cílem bylo vytvořit modul, který bude mechanicky odolný, aerodynamicky krytý a nebude trpět přenosem vibrací z motorů nosiče.

> Obrázek 5 — Render osazeného držáku komunikačního modulu

### 5.1 3D tištěný držák elektroniky

Pro centrální upevnění všech prvků byl v CAD softwaru Fusion 360 navržen dedikovaný držák. Ten byl následně vytištěn na 3D tiskárně z materiálu PETG. Tento materiál byl zvolen pro svou vyšší tepelnou odolnost a mechanickou houževnatost ve srovnání s běžným PLA, což je pro letecké aplikace klíčové.

Držák funguje jako nosná kostra celého modulu. Pro zajištění proudění vzduchu pro chlazení vysílacího modulu byl v držáku navržen prostor pro proudění vzduchu z větráku aktivního chlazení modulu.

> Obrázek 6 — Render osazeného držáku komunikačního modulu

### 5.2 Ochrana a aerodynamický kryt

Modul byl následně vložen do ochranného obalu vyrobeného z expandovaného polypropylenu (EPP). Tento materiál byl zvolen pro své vynikající tlumicí vlastnosti. EPP obal slouží hlavně jako mechanická ochrana proti poškození při případném tvrdém přistání a proti nepřízni počasí.

Tento EPP obal byl aerodynamicky vytvarován, aby minimalizoval odpor vzduchu. Byl poté vyříznut horkým drátem dle šablony a pokryt nažehlovací potahovou fólií.

> Obrázek 7 — Pohled na osazený držák v EPP obalu
> Obrázek 8 — Aerodynamický tvar EPP obalu
---

### 6. Testování a letové zkoušky

Pro ověření funkčnosti celého systému a splnění cílů práce byl projekt podroben sérii testů, od laboratorního zkoušení na stole až po nasazení v reálném letovém provozu.

### 6.1 Laboratorní zkoušky (Bench testy)

Před samotným nasazením do letounu proběhla fáze pozemního testování. Cílem bylo ověřit stabilitu firmwaru, správné formátování CRSF rámců a spolehlivost half-duplexního přepínání komunikační sběrnice. Systém byl propojen s řídicí jednotkou letounu a hodiny byl testován na nepřetržitý tok dat.

Během těchto testů byla rovněž ověřena logika diagnostického webového rozhraní. Odpojováním jednotlivých komponent bylo simulováno přerušení spojení, na což dashboard okamžitě a korektně reagoval zobrazením varovných stavů (RC LOST, MODULE OFF, DRONE LOST). Ačkoliv absolutní hodnota přidané latence nebyla exaktně měřena přístroji, díky zpracování dat na dedikovaném jádře nebylo při ovládání letounu na zemi pozorováno žádné subjektivní zpoždění reakcí servomotorů ani regulátorů.

### 6.2 Integrace do vynášecího letounu

Pro vzdušnou retranslaci bylo nutné modul bezpečně upevnit na vynášecí letoun. Byl využit dedikovaný držák, který zajišťuje pevné uchycení desky elektroniky i obou rádiových modulů. Celý modul byl napájen vlastní nezávislou 2S LiPo baterií, což zaručilo bezpečné oddělení energetických nároků vysílače od letových systémů dronu.

### 6.3 Reálné letové testy a zhodnocení dosahu

Klíčovým bodem celého projektu byla validace systému v reálném prostředí. Běžný efektivní dosah řídicího spojení při dodržení evropských legislativních limitů vysílacího výkonu se v testovací lokalitě (členitý terén s překážkami) pohyboval na hranici 1 km. Za touto hranicí již docházelo ke ztrátě kvality spojení.

Při testech se podařilo udržet spojení na vzdálenostech přes 2 km.

V letových testech se také ověřila schopnost letadla vypustit modul v reálných podmínkách. Těmito testy byly úspěšně naplněny hlavní cíle maturitní práce – bezpečné a minimálně dvojnásobné rozšíření komunikačního dosahu. Z pohledu pilota bylo ovládání stroje přes retranslační uzel naprosto transparentní, bez výpadků a pocitově bez nárůstu zpoždění řízení.

---

### 7. Závěr

Tato práce se zabývala návrhem a realizací retranslačního uzlu (komunikačního modulu) pro bezpilotní letouny s cílem překonat legislativní a fyzikální omezení dosahu rádiového řízení. Výsledkem je plně funkční a nezávislé zařízení postavené na mikrokontroléru ESP32, které funguje jako transparentní most mezi vstupním 2.4 GHz přijímačem a výkonným 900 MHz vysílačem ekosystému ExpressLRS.

Klíčovým přínosem hardwarového řešení je návrh vlastní desky plošných spojů vybavené bufferem SN74HC125DR, který úspěšně překonává hardwarovou nekompatibilitu a umožňuje plynulou half-duplexní komunikaci s vysílacím modulem. Po softwarové stránce se podařilo maximalizovat spolehlivost využitím asymetrického rozdělení zátěže na obě jádra procesoru. Dedikované jádro pro rádiovou komunikaci zajistilo bezchybný chod s neznatelnou latencí, zatímco druhé jádro obsluhuje integrovaný webový dashboard, který se ukázal jako neocenitelný nástroj pro předletovou diagnostiku a čtení telemetrie.

Praktické letové zkoušky potvrdily správnost navržené koncepce. Integrovaný systém prokazatelně zdvojnásobil bezpečný dosah řízení na vzdálenost 2 km v náročném terénu, a to bez jakýchkoliv výpadků či ztráty plynulosti ovládání.

Vyvinutý ESP32-CRSF-Relay modul tak stoprocentně naplnil cíle maturitní práce. Představuje vysoce funkční, spolehlivé a kompaktní řešení pro bezpečný provoz UAV na delší vzdálenosti, které by v budoucnu mohlo být dále rozšířeno například o ukládání telemetrických dat na SD kartu.

---

### Poděkování

Rád bych poděkoval vedoucímu své maturitní práce, panu Ing. Adamu Ferenczovi, za vedení, které mi poskytl během vývoje tohoto projektu.
