Maturitní projekt - Gymnázium Havlíčkův Brod - 2026 Bezpilotní letoun se schopností vertikálního vzletu a přistání, schopný přenášet komunikační modul

Mark Joly

Abstrakt Tato práce se věnuje návrhu a realizaci bezpilotního letounu s překlopnými rotory (tiltrotor) s funkcí vertikálního vzletu a přistání (VTOL). Hlavním cílem projektu je konstrukce plně funkčního prototypu, který kombinuje výhodu statického tahu rotorů s aerodynamickou efektivitou křídla při nesení užitečného zatížení v podobě 250g komunikačního modulu. Konstrukce využívá materiály, jako jsou uhlíkové kompozity a EPP pěna, doplněné o komponenty vyrobené technologií 3D tisku. K řízení letounu a stabilizaci přechodových manévrů slouží systém ArduPilot. Práce dokumentuje kompletní vývojový cyklus – od volby koncepce a modelování v CAD prostředí přes integraci elektroniky až po finální letové zkoušky, které ověřily stabilitu, maximální rychlost a dolet stroje při plném zatížení.

Gymnázium Havlíčkův Brod

### 1. Úvod

### 1.1 Popis problému a motivace

V současné sféře bezpilotních prostředků (UAV) existuje výrazná propast mezi efektivitou letu a operační flexibilitou. Zatímco klasické koptéry umožňují precizní operace v omezeném prostoru, jejich energetická náročnost limituje dosah. Letadla s pevným křídlem sice nabízejí dlouhý dolet, ale vyžadují rozsáhlou infrastrukturu pro vzlet a přistání.

Klíčovým problémem, který tato práce řeší, je doprava a aktivace komunikační infrastruktury v těžko přístupných nebo rozsáhlých oblastech, kde terénní překážky či vzdálenost znemožňují přímé rádiové spojení s řídicí stanicí. Současnářešeníčastoselhávajíbuďnaneschopnosti přesného doručení do cílového bodu bez poškození nákladu, nebo na nízké efektivitě přepravy.

### 1.2 Cíle projektu: Hardwarový Proof of Concept

Hlavním záměrem práce je vývoj a experimentální ověření funkčnosti hardwarové platformy typu QuadPlane Tilt-rotor. Projekt slouží jako Proof of Concept (PoC),kterýdemonstrujemechanickouaelektronickou integraci systémů schopných zajistit transportní mise v

náročných podmínkách. Cíle projektu byly definovány jako:

- Vývoj a validace VTOL platformy: Konstrukce
letounu s hybridním pohonným systémem, který
v rámci jedné konstrukce integruje stabilitu koptéry pro vertikální manévry a aerodynamický vztlak křídla pro efektivní dopředný let.
- Demonstrace transportního cyklu: Návrh hardwaru a mechanismů pro kompletní operační
sekvenci: vertikální vzlet se zátěží 250 g, přechod
do dopředného letu, vertikální přistání v cílové
lokaci,mechanickéodpojeníkomunikačníhomodulu a následný vzlet bez zátěže.
- Konstrukčníoptimalizaceaintegrace: Dosažení
vyváženého poměru mezi strukturní tuhostí a
hmotností letounu za využití kompozitních materiálů a technologie 3D tisku, s cílem zajistit
bezpečné nesení užitečného zatížení.
- Stabilizacekritickýchletovýchfází: Softwarová
integrace a naladění řídicích algoritmů pro
bezpečné zvládnutí přechodu (transition) mezi
dvěma fyzikálně odlišnými režimy letu, což je
klíčový technický milník pro stabilitu celého konceptu.

Obrázek 1. VTOL letoun během jednoho z letů.

Tento Proof of Concept tak představuje hmatatelný základ pro další rozvoj specializovaných UAV systémů, kde je kladen důraz na mechanickou odolnost a schopnost doručovat technologii do míst bez nutnosti vzletové dráhy.

### 2. Volba koncepce a aerodynamická analýza

### 2.1 Výběr konfigurace: Twin-boom a H-tail

Pro zajištění maximální stability během vertikálního vzletu i dopředného letu byla zvolena koncepce Twinboom s ocasními plochami uspořádanými do tvaru H-tail. Tato struktura nabízí několik zásadních výhod:

- Vysoká torzní tuhost: Dvojitý nosník ocasních
ploch efektivně rozkládá síly působící na trup.
- Směrová stabilita: Dvě svislé ocasní plochy (Htail) umístěné přímo v proudu vzduchu od předníchmotorůzajišťujívynikajícíovladatelnostsměru
i při nízkých rychlostech během přechodové fáze.
- Prostorová efektivita: Umožňuje čistou integracizadníchmotorůachráníocasníplochypřed
vibracemi a turbulencemi v režimu koptéry.

Obrázek 2. Render celkové struktury letounu z čelního pohledu (vytvořeno v Autodesk Fusion 360).

### 2.2 Hmotnostní rozvaha a rozměry

Základní geometrie letounu je definována rozpětím 1600 mm. Celková hmotnost stroje byla pro účely výpočtů rozdělena na tři hlavní složky:

- Drak: 2100 g (zahrnuje konstrukci a elektroniku).
- Akumulátor: Hmotnost napájecího zdroje se liší
dle zvolené kapacity, což umožňuje flexibilní nastavení poměru mezi doletem a dynamikou stroje.
- Užitečné zatížení: Až 250 g (Koncipováno pro
přenos komunikačního modulu)

Při uvažované vzletové hmotnosti se plošné zatížení pohybuje v ideálním rozmezí pro stabilní let i při vyšší okolní turbulenci.

### 2.3 Výběr aerodynamických profilů

Klíčovým prvkem pro zvládnutí přechodu (transition) mezi visením a letem je volba profilů schopných generovat vztlak i při nízkých rychlostech:

- Křídlo (NACA 4415): Tento prohnutý profil s
tloušťkou15 %bylzvolenprosvůjvysokýsoučinitel vztlaku a velmi mírné pádové charakteristiky.
Tloušťka profilu navíc poskytuje dostatečný prostor pro vložení uhlíkových výztuh. Tady je ta věta
v odborném stylu, kterou můžeš vložit do podkapitolyokřídle:„Prozvýšeníaerodynamickéefektivity a zajištění dostatečného vztlaku při vodorovné orientaci trupu během dopředného letu byl
profil křídel nastaven pod úhlem seřízení (angle
of incidence) 2◦vůči podélné ose stroje.
- Ocasní plochy (NACA 0012a NACA 0015):
Symetrické profily zajišťují minimální odpor a

lineární odezvu na zásahy kormidel, což usnadňuje práci stabilizačním algoritmům programu ArduPilot.

Obrázek 3. Geometrie profilu křídla NACA 4415.

Při návrhu byl kladen důraz na to, aby letoun neztrácel stabilitu v momentě, kdy se vektor tahu motorů sklápí vpřed a křídlo začíná postupně přebírat nosnou funkci. Právě tlustší profil NACA 4415 zaručuje, že nedojde k náhlému odtržení proudění.

### 3. Návrh a realizace elektroniky

### 3.1 Výběr řídicí jednotky

Řídicí jednotka (Flight Controller) představuje mozek celého stroje. Pro tento projekt byl vyžadován hardware s vysokou výpočetní kapacitou a širokou konektivitou pro periferie.

3.1.1 Existující typy a potřeby projektu

Při výběru se rozhodovalo mezi různými open-source platformami. Hlavním kritériem byla plná podpora firmware ArduPilot a dostatek hardwarových PWM výstupů pro ovládání hybridního systému motorů a serv.

3.1.2 Zvolené řešení:

Byla zvolena jednotka SpeedyBee F405 Wing APP. Tato deska integruje výkonný procesor, PDB (Power Distribution Board) a silné BEC okruhy pro napájení velkého počtu serv. Výhodou je bezdrátový management, který usnadňuje konfiguraci v terénu.

### 3.2 Výběr pohonných jednotek

Pohonná soustava je rozdělena na přední naklápěcí motory a zadní pevné motory, což vyžadovalo specifický výběr komponent pro každý pár.

3.2.1 Přední motory a vrtule

Pro přední část byly zvoleny motory Flash Hobby EVO2826 (1000KV) osazené vrtulemi o rozměru 9×5. Tyto motory zajišťují hlavní tah při vertikálním vzletu i dopředném letu po překlopení.

3.2.2 Zadní motory a vrtule

ZadníčástvyužívámotoryLeopardLC2826-17T(900KV) s vrtulemi 11×5. Tato kombinace poskytuje potřebnou stabilitu v režimu koptéry.

3.2.3 Regulátory (ESC)

K regulaci otáček slouží čtyři jednotky Flycolor FlyDragon30A.Jednáseoopto-izolovanéregulátory(oddělená zem a signál), což minimalizuje elektromagnetické rušení v řídicí elektronice.

### 3.3 Výběr napájení

Napájecí systém je navržen pro vysoké proudové zatížení při startu VTOL. Jako zdroj energie slouží akumulátory Kavan / BigHobby 4S Li-Po. Dle typu mise lze volit mezi kapacitou 3250 mAh pro nižší hmotnost nebo 5200 mAh pro delší vytrvalost.

3.3.1 Zapojení napájení

Napájení je z akumulátoru distribuováno skrze SpeedyBee desku k jednotlivým ESC. Systém je doplněn o GPS modul HGLRC M100-5883 s protokolem u-blox M10 a integrovaným kompasem pro přesnou orientaci v prostoru.

Obrázek 4. Zapojení periferií k řídicí jednotce.

### 3.4 Výběr ovládacích systémů (Servomechanismy)

Vzhledem k počtu 9 serv byla zvolena kombinace digitálních serv s různým tahem dle jejich funkce:

- Tilt serva: 2× BH Servo 3370 (Digital) s tahem
20 kg/cm pro spolehlivé naklápění předních motorů.
- Křidélka: 2× JX PDI-HV2107MG (Slim) s tahem
8 kg/cm.
- Ocasní plochy: 3× Corona DS843MG (Digital)
s tahem 4,8 kg/cm pro výškovku a směrovky.
- Mechanismus modulu: 2× serva zajišťující manipulaci s komunikačním modulem.

### 4. Návrh prostřednictvím CAD

### 4.1 Výhody návrhu v CAD prostředí

Vzhledem ke komplexnosti mechaniky Quad-Plane Tiltrotoru byla práce v CAD (Computer-Aided Design)

prostředí naprosto nezbytná. Umožnila totiž vyřešit kritické aspekty konstrukce ještě před samotným nákupem materiálu:

- Kinematika naklápění: Simulace pohybu motorovýchgondolověřila, ževžádnéfázipřechodu
nedocházíkekolizivrtulísnáběžnouhranoukřídla
nebo trupem.
- Iterativnívývojtěžiště(CoG):UVTOLletounuje
těžiště pohyblivým cílem. CAD umožnil precizní
rozmístění těžkých komponent (akumulátor, motory) tak, aby se výsledné těžiště shodovalo s
ideálním středem tahu v režimu visení i s aerodynamickým středem v režimu letu.
- Přesnost montážních bodů: Všechny otvory
prouhlíkovénosníkyauloženíservbylynavrženy
s nulovou tolerancí pro následný 3D tisk, což zajistilo vysokou strukturální integritu bez vůlí.

### 4.2 Výběr CAD softwaru

Jako hlavní nástroj byl zvolen Autodesk Fusion 360. Tentosoftwarebylpreferovánprosvépokročilénástroje pro parametrické modelování a vynikající správu sestav. Cloudová architektura umožnila efektivní správu verzí, zatímco integrovaný modul pro renderování poskytl fotorealistické náhledy sloužící k vizuální kontrole proporcí stroje.

### 4.3 Proces návrhu základního tvaru

Postup návrhu byl striktně hierarchický a vycházel z vnější aerodynamické obálky směrem k vnitřním detailům:

### 1. Skeleton křídla a nosníků: Prvním krokem bylo definování rozpětí 1600 mm a délky trupu. Na tyto osy byly vyneseny profily NACA 4415 (křídlo) a NACA 0012 (ocasní plochy). 2. Návrh centrální gondoly: Trup byl modelován tak, aby pojal nejen řídicí elektroniku, ale i specifický prostor pro komunikační modul a mechanismus jeho uvolnění. 3. Integrace komponent: Do modelu byly vloženy reálné rozměry motorů a akumulátorů z technické dokumentace. Tento krok byl klíčový pro finální vyvážení celého stroje.

Digitální model posloužil jako přímý podklad pro generování dat pro 3D tisk a výrobu šablon pro řezání EPP, čímž byla zaručena absolutní shoda mezi návrhem a realitou.

### 5. Návrh součástí a výroba

Obrázek 5. Komplexní digitální sestava letounu vytvořená v prostředí Fusion 360.

### 5.1 Konstrukce nosného karbonového skeletu

Základní nosnou strukturu letounu tvoří prostorový rám z pletených uhlíkových kompozitních trubek (vzor 3K). Tento materiál byl zvolen pro svou superiorní pevnost v krutu oproti běžným pultrudovaným profilům.

5.1.1 Příprava materiálu a geometrické lícování

Klíčem k vysoké pevnosti skeletu bylo precizní lícování spojů. Konce trubek (hlavní nosníky 15/13 mm a ocasní nosníky 10/8 mm) byly vybroušeny do rádiusů odpovídajících průměru navazujících prvků, čímž bylo dosaženo maximální styčné plochy pro následné spojování.

5.1.2 Metodika spojování a strukturální laminace

Kompletace rámu probíhala ve dvou fázích s využitím 3D tištěných montážních úchytů (jigs) pro zajištění absolutní souososti:

### 1. Fixace (Bodování): Prvotní spojení lícovaných trubek bylo provedeno dvousložkovým 5minutovým epoxidem Kavan. 2. Strukturální laminace: Po mechanickém zdrsnění povrchu a odmaštění izopropylalkoholem byly spoje olaminovány uhlíkovým rovingem (12K) v kombinaci s vysokopevnostní pryskyřicí Epoxy L285. Tato metodavytvářímonolitickéuzlysextrémnítuhostí.

### 5.2 Integrace pomocných konstrukcí a 3D tisk

Všechnydržákyelektronikyaservbylyvyrobenymetodou FDM na tiskárně Bambu Lab P1S z materiálu PETG.

- Konfigurace tisku: Byla využita 30% výplň s geometrií Gyroid pro rovnoměrné rozložení sil a 4
obvodové vrstvy pro pevnost montážních bodů.
- Spojenísrámem: Tištěnédíly(pro9servaavioniku)
slouží jako lůžka, která byla následně rovněž
olaminována k uhlíkovému rámu rovingem a
pryskyřicí L285.

Obrázek 6. Sestavená uhlíková kostra.

Obrázek 7. Detail zalaminovaného spoje.

### 5.3 Mechanismusvektorovánítahu(Tilt-mechanism)

Mechanismus naklápění předních motorů musel eliminovatvůleazvládnoutvysokévibrace. Namístopřímého uloženínatisícihranuservabylazvolena**dvoubodová podpora osy**:

- Aktivní strana: Digitální servo JX PDI-2506MG.
- Opěrná strana: Kuličkové ložisko vlisované do
PETG držáku, v němž je uložena nerezová osička.
- Překlopný člen: Vlastní lože motoru je vyrobeno
zhliníkovéhoplechu(1,5 mm), kterýplnífunkci
pasivního chladiče a zajišťuje tuhý přenos tahu
motoru do rámu.

Obrázek 8. Překlopný mechanismus předních motorů (render).

### 5.4 Výroba aerodynamických ploch z EPP

Pro křídla a trup byl zvolen extrudovaný polypropylen (EPP) pro jeho tvarovou paměť a odolnost proti nárazům.

5.4.1 Vlastní odporová řezačka

Pro dosažení přesnosti profilu NACA 4415 byla zkonstruovánazakázkovářezačkasmechanickýmpředpětím drátu pomocí ocelového lanka. Jako zdroj byl použit transformátor ZVS Dubnica. Tepelný výkon byl kalibrován tak, aby docházelo k plynulému propalování materiálu bez mechanického tlaku na drát.

5.4.2 3D tištěné šablony

Křídla byla řezána podle 3D tištěných šablon z PLA, jejichž hrany byly chráněny hliníkovou fólií pro snížení tření a tepelnou ochranu.

Obrázek 9. Odporová řezačka.

Obrázek 10. Šablona na vyříznutí křídel.

### 5.5 Finalizace

- Kompletace: Segmenty trupu a křídel byly spojovány expandujícím PU lepidlem, které vyplnilo
póry EPP.

Obrázek 11. Šablona na vyříznutí směrového kormidla.

- Povrchováúprava: Povybroušenínízkoexpanzní
montážní pěny v místech spojů byl celý povrch
potažen vinylovou fólií. Ta plní funkci vnější
nosnéslupky(stressedskin),čímžvýraznězvyšuje
torzní tuhost celého letounu a zlepšuje aerodynamiku povrchu.

### 6. Softwarová konfigurace a řízení

### 6.1 Firmware a řídicí logika

Pro autonomní řízení a stabilizaci letounu byl zvolen systém ArduPilot (větev ArduPlane). Klíčovým prvkem je aktivace modulu QuadPlane (Q_ENABLE = 1), který umožňuje kombinovat letové charakteristiky koptéry a plošníku.

Základní architektura stroje byla definována jako Quad (Q_FRAME_CLASS = 1) v uspořádání X-frame (Q_FRAME_TYPE = 1). Vzhledem k absenci fyzického senzoru rychlosti (pitotovy trubice) je systém nastaven na výpočet syntetické rychlosti (ARSPD_USE = 0) pomocí fúze dat z GPS a inerciálních senzorů v algoritmu EKF3 (EK3_ENABLE = 1).

### 6.2 Konfigurace Tilt-Rotor mechanismu

Nejdůležitější částí softwarového nastavení je definice vektorování tahu. Na základě experimentálního ladění byly stanoveny následující klíčové parametry:

- Definice pohyblivých os: Pomocí parametru
Q_TILT_MASK = 5 (binárně 101) bylo určeno, že
serva naklápějí motor č. 1 a č. 3 (přední motory).
- Asymetrickádynamikanaklápění: Prozajištění
stability byl nastaven rozdílný poměr rychlosti
naklápění. Přechod do dopředného letu je agresivní (Q_TILT_RATE_UP = 80 °/s) pro rychlé
získání vztlaku křídla, zatímco návrat do visu je

plynulejší (Q_TILT_RATE_DN = 20 °/s) pro eliminaci náhlého pitch-up momentu. • Vektorování směru (Yaw): Pro stabilizaci kolem svislé osy v režimu visu je využito naklápění motorů v rozsahu 12° (Q_TILT_YAW_ANGLE = 12), což nahrazuje chybějící reakční momenty křížového uspořádání rotorů.

### 6.3 Fáze přechodu (Transition)

Procestransitionjekritickýmmomentemletu. Parametr Q_TRANSITION_MS = 6000 definuje šestisekundové okno,běhemkteréhodocházíkpostupnémupředávání autority z rotorů na aerodynamická kormidla.

- Bezpečné rychlosti: Minimální rychlost pro
ukončení přechodu byla stanovena na 9 m/s
(AIRSPEED_MIN = 9), zatímco cestovní rychlost
byla definována na 12 m/s (AIRSPEED_CRUISE
= 12).
- Asistence koptéry: V případě poklesu rychlosti
nebo ztráty vztlaku je aktivována asistence koptérypřináklonunad30°(Q_ASSIST_ANGLE = 30),
která automaticky aktivuje vertikální motory pro
záchranu stroje.

### 6.4 Letové režimy a správa energie

Letoun využívá širokou škálu režimů konfigurovaných na přepínači kanálu 7 (FLTMODE_CH = 7):

Režim Charakteristika QHOVER Plně manuální visení bez GPS fixace. QLOITER Visení s automatickým držením pozice pomocí GPS. FBWA Stabilizovaný dopředný let s omezením náklonů. AUTOTUNE Režim pro automatické ladění PID hodnot za letu.

Tabulka 1. Konfigurace letových režimů extrahovaná z parametrů stroje.

Správa napájení je kalibrována pro 4S Li-Po akumulátor s kapacitou 5200 mAh (BATT_CAPACITY = 5200). Proudovýsenzorjenastaven na 50 A na volt (BATT_AMP_PERVLT = 50), což zajišťuje přesnoutelemetriiozbývajícíenergiiběhemtransportní mise.

### 7. Testování a ladění za letu

Proces uvádění letounu do provozu byl rozdělen do několika fází, od statických zkoušek až po plně automatizovaný přechod do dopředného letu.

### 7.1 Předletová příprava a první vzlety

Před prvním vzletem byla provedena kompletní kalibrace všech klíčových senzorů v prostředí Mission Planner. Jednalo se o:

- Kalibraci IMU a kompasu: Nezbytné pro správnou orientaci v prostoru a funkci GPS režimů.
- Kalibraci rádia a ESC: Nastavení rozsahů PWM
signálů pro motory a ovládací prvky.

První testovací lety probíhaly v manuálním režimu QSTABILIZE.Běhemtěchtotestůseukázalo,žeotáčení kolem svislé osy (yaw) pouze pomocí rozdílných otáček rotorůneníutétogeometriedostatečněefektivní. Problém byl vyřešen aktivací funkce Vectored Yaw, která pro rotaci využívá naklánění předních motorů proti sobě. Poté již byla odezva na řízení směru okamžitá a přesná.

### 7.2 Stabilizace výšky a první kritický transition

Následně byl testován režim QHOVER. V tomto režimu letoun automaticky udržoval nastavenou výšku, což výrazně usnadnilo ovládání, zejména při bočních manévrech, kdy stroj neztrácel výšku vlivem náklonu.

Kritickým bodem testování byl pokus o přechod do letadlového režimu (FBWA). Při prvním pokusu však došlo k havárii z následujících příčin:

### 1. Chybějící asistence: Nebyla aktivována pomoc zadních motorů během přechodové fáze. 2. Příliš rychlé naklopení: Přední motory se překlopily do horizontální polohy okamžitě, aniž by letoundosáhldostatečnépádovérychlostikřídla.

### 7.3 Optimalizace parametrů a úspěšný let

Poopravěpoškozenýchčástíbylaprovedenahloubková revize Q-parametrů. Byla nastavena asistence zadních motorů (Q_ASSIST), která pomáhá stabilizovat letoun, pokud jeho rychlost klesne pod kritickou hranici (AIRSPEED_MIN). Doba překlopení motorů byla prodlouženaproplynulejšínárůstvztlakunakřídle. Zároveň bylo nakonfigurováno plynulé navracení motorů do vertikální polohy při zpomalování.

Tyto úpravy vedly k plně stabilnímu dopřednému letu. Následné testy s nákladem komunikačního modulu v gondole proběhly bez komplikací, přičemž zvýšená hmotnost neměla výrazný vliv na dynamiku přechodu.

### 7.4 Finální ladění a autonomie

V poslední fázi byl zprovozněn režim QLOITER, který díky GPS fixaci drží přesnou pozici a směr i v nárazovém větru. Stabilizace byla dále zjemněna během několika letů, kdy letoun v poloautomatickém režimu částečně

adaptovalsvéPIDhodnoty(In-flighttuning). Vsoučasné konfiguraci vykazuje stroj vysokou míru stability ve všech letových fázích.

### 8. Závěr

Předložená práce dokumentuje kompletní proces vývoje bezpilotního letounu typu VTOL v konfiguraci Quad-Plane Tilt-rotor. Během realizace se podařilo úspěšně propojit pokročilé metody digitálního návrhu, 3D tisku z polymerů a strukturální laminace uhlíkovým rovingem, čímž vznikl stroj s vysokou tuhostí a nízkou hmotností.

Klíčovým přínosem práce bylo odladění softwarového řízení v systému ArduPilot. Přes počáteční komplikace spojené s dynamikou přechodové fáze letu (transition) se podařilo nastavením asistenčních algoritmů a vektorovánítahudosáhnoutplnéstabilityvevšechletových režimech. Testy s nákladem prokázaly, že letoun je schopen bezpečně plnit svou primární funkci – transport a doručení komunikačního modulu.

Tento projekt posloužil jako úspěšný technologický demonstrátor. Do budoucna se nabízí prostor pro další vylepšení, zejména v oblasti plné autonomie letu a integrace přesnějšího senzoru rychlosti. Výsledný stroj je však již v současném stavu spolehlivou platformou, která potvrzuje efektivitu zvolené koncepce pro moderní bezpilotní logistiku.

### Poděkování

Rád bych poděkoval vedoucímu své maturitní práce, panuIng. AdamuFerenczovi,zavedení,kterémiposkytl během vývoje tohoto projektu