Maturitní projekt - Gymnázium Havlíčkův Brod - 2026 Webová aplikace pro správu a distribuci školních propagačních předmětů

Jakub Jakůbek

Abstrakt Článek popisuje návrh a realizaci webové aplikace pro správu a distribuci školních propagačních předmětů, která digitalizuje proces hromadných objednávek školního oblečení na Gymnáziu Havlíčkův Brod. Představuje analýzu původního stavu, koncepty uživatelského rozhraní a výsledky testování použitelnosti, které prokázaly zkrácení objednávkového procesu z přibližně deseti minut na méně než dvě minuty.

Gymnázium Havlíčkův Brod

### 1. Úvod

Objednávání školního oblečení – triček, mikin či doplňků s logem školy – je na středních školách tradiční a velmi oblíbený rituál, který posiluje pocit sounáležitosti se školou. Na Gymnáziu Havlíčkův Brod probíhal po léta sběr těchto objednávek primárně přes Google Formuláře. Ačkoliv se na první pohled může jednat o moderní a snadno dostupné řešení, v praxi se ukázalo jako značně nepřívětivé a neefektivní z hlediska škálovatelnosti.

Typický dotazník obsahoval předlouhý výčet všech produktů, navíc se všemi myslitelnými variantami barev a velikostí. Student musel zdlouhavě scrollovat desítkami položek, hledat tu správnou kombinaci a doufat, že v záplavě textu nic nepřehlédl. Horší však bylo to, že po odeslání formuláře neměl objednatel absolutně žádnou možnost zjistit, co se s jeho objednávkou děje. Nevěděl, zda se vůbec nasbíral dostatečný počet kusů pro výrobu, kdy se oblečení zadá dodavateli, nebo kdy a kde bude připraveno k vyzvednutí. Vznikalo tak komunikační vakuum, které vedlo k častým dotazům na vedení školy či studentskou radu.

Z pohledu školních administrátorů (často z řad studentské rady nebo pověřených učitelů) byla situace podobně, ne-li více, frustrující. Odpovědi z formuláře bylo nutné ručně zpracovávat v nepřehledných tabulkách. Bylo třeba složitě počítat, zda byl dosažen minimální počet kusů pro tisk určité barvy, a při samotném výdeji pak identifikovat konkrétní objednávku jen podle jména na vytištěném papírovém seznamu. Navíc samotný sběr probíhal pouze v omezeném časovém okně – formulář se na několik týdnů otevřel a následně nevratněuzavřel. Kdosinestihlmikinuobjednat,musel čekat na další rok.

Cílem tohoto projektu bylo celý tento zastaralý proces kompletně nahradit moderní webovou aplikací. Ta měla umožnit studentům pohodlně prohlížet jednotlivé produkty včetně jejich vizuálních variant, sledovat stav své objednávky v reálném čase a především – objednávat kdykoli v průběhu celého školního roku.

Na trhu sice existuje celá řada robustních e-shopových platforem (např. Shopify, Shoptet, WooCommerce), avšak takřka žádná z nich nativně nepodporuje specifický koncept takzvaného hromadného sběru objednávek bez okamžité platby, kde se produkty zadávají do hromadné výroby až po dosažení určitého minimálního počtu kusů. Nástroje jako Google Formuláře sice umožňují elementární sběr dat, ale postrádají katalog s vizuálními variantami, automatizaci stavů, e-mailové notifikace i nástroje pro ověřování výdeje. Právě tato funkční mezera motivovala vznik zcela vlastního řešení na míru potřebám školy.

Výsledkem projektu je moderní full-stack webová aplikace postavená na populárním frameworku SvelteKit, navržená tak, aby byla rychlá, snadno spravovatelná a plně vyhovovala zvyklostem dnešních uživatelů internetu.

### 2. Analýza objednávkových procesů

Před samotným návrhem nové aplikace bylo nezbytné detailně zmapovat a analyzovat stávající situaci. Pouze pochopením chyb a úzkých hrdel (tzv. bottlenecks) starého systému bylo možné navrhnout smysluplnou inovaci a zajistit, že nový systém nebude pouze „hezčí verzí“ téhož, ale že reálně usnadní práci.

### 2.1 Identifikace slabých míst původního systému

Původní workflow vypadal zhruba takto: Administrátor vytvořil Google Formulář se statickým seznamem všech produktů a jejich variant. Odkaz na formulář se následněsdílelnasociálníchsítíchaškolníchnástěnkách. Odpovědi se hromadily v tabulce. Po manuálním uzavření sběru musel administrátor provést ruční deduplikaci, zkontrolovat nesmyslné zadání a agregovat

počtykusůprododavatele, cožnezřídkatrvaloiněkolik dnů.

Hlavní problémy identifikované během analýzy lze shrnout do následujících bodů:

- Vysoká kognitivní zátěž uživatele: Jeden
dlouhý seznam všech produktů bez přehledné
vizuálníprezentacenutiluživatelepřílišpřemýšlet
a číst
textové popisky (např. „Mikina s kapucí - Námořnická modrá“) místo přímé vizuální volby.
- Absencestavovézpětnévazby: Studentpoodeslání
žil v informačním vakuu. Nevěděl, zda byla objednávka přijata, ani v jaké fázi zpracování se
nachází.
- Nárazovostaexkluzivita: Časověomezenýsběr
vytvářelzbytečnýstresavyřazovalstudenty,kteří
napříkladvdanémtýdnuchybělizdůvodunemoci.
- Značnáchybovostanáročnostproadministrátory: Tabulkový proces vyžadoval hodiny ruční
práce a byl extrémně náchylný na lidskou chybu,
zvláštěpřifinálnímvýdejizbožístovkámstudentů,
kdysečastoprohazovalyobjednávkypodobných
jmen.

### Obrázek 1. Původní objednávkový formulář (jedna položka)

### 2.2 Nový koncept: Kontinuální sběr a Batch systém

Zásadním specifikem výroby školního merche je technologiepotisku(nejčastějisítotisk),ukteréplatínepřímá

úměra mezi počtem kusů a cenou. Pro dodržení dostupnécenyjenutnévyrobitvždyurčitýminimálnípočet kusů se stejným designem a barvou najednou.

Abychom vyřešili problém časového omezení objednávání a zároveň plně respektovali nutnost vyrábět oblečení hromadně, byl navržen systém hromadných dávek (Batch systém).

Studenti mohou v nové aplikaci objednávat nepřetržitě po celý rok. Tyto individuální objednávky aplikace na pozadí automaticky seskupuje do takzvané aktivní dávky (batch). Jakmile administrátor v systému vidí, že celkový počet kusů v aktuální dávce dosáhl rentabilního minima, dávku v systému uzamkne. Od toho okamžiku se již do této dávky nedají přidávat nové položky a celá dávka je exportována pro dodavatele kvýrobě. Tímtouzamčenímsevšakvsystémuokamžitě automaticky otevírá dávka nová pro další zájemce. Zákaznická zkušenost z objednávání tak není nikdy přerušena.

Aby tento systém fungoval i psychologicky, byl do uživatelského rozhraní integrován dynamický ukazatel průběhu (Progress bar). Ten vizuálně ukazuje, jaká část z minimálního počtu kusů je již naplněna. Funguje to jako silný motivační prvek – pokud student vidí, že do odeslání objednávky dodavateli chybí už jen několik málo kusů, má tendenci proces urychlit, případně motivovat své spolužáky k nákupu, aby se objednávka mohla co nejdříve zrealizovat.

### 2.3 Životní cyklus objednávky

Druhou zásadní inovací je transparentní stavový automat pro každou jednotlivou objednávku. Od momentu vytvoření košíku až po předání do rukou studenta prochází objednávka jasně vymezenými stavy:

### 1. Zapsáno: Objednávka je úspěšně uložena v databázi systému, zařazena do aktivní dávky a čeká na její naplnění a uzavření. 2. Ve výrobě: Dávka, do které objednávka patří, byla uzavřena, odeslána dodavateli a oblečení se aktuálně potiskuje a kompletuje ve výrobní hale. 3. Připraveno: Zbožídorazilozvýrobyzpětdoškoly, administrátořijejroztřídiliaoblečeníjepřipraveno k fyzickému vyzvednutí. 4. Vyzvednuto: Koncový stav, do kterého je objednávka přepnuta ve chvíli, kdy si student oblečení fyzicky převzal a vyrovnal finanční závazky.

Při každém z těchto přechodů systém automaticky vygeneruje a odešle e-mailovou notifikaci. Student je tak proaktivně informován, získává jistotu, že se na jeho

objednávce pracuje, a nemusí se dotazovat administrátorů na aktuální stav.

### Obrázek 2. Stav objednávky zobrazovaný v aplikaci

### 3. Návrh uživatelského rozhraní a UX

Aplikace navržená pro středoškoláky musí být v první řaděvizuálněpřehledná,moderníasnadnoovladatelná i z mobilních zařízení. Z toho důvodu byl kladen velký důraz na celkové User Experience (UX), které přímo odstraňuje největší bolesti předchozího řešení. Aplikace byla navrhována tak, aby nepůsobila jako strohý školní informační systém, ale spíše jako plnohodnotný komerční produkt.

### 3.1 E-shopový standard místo dotazníku

Nejvýraznějším rozhodnutím bylo naprosté opuštění formulářového paradigmatu. Současná generace uživatelů je zvyklá nakupovat na internetu pomocí standardizovaných postupů, a proto tento projekt do svého rozhraní plně adoptoval vizuální a funkční vzory známé z běžných e-shopů.

Katalogproduktůjelogickyrozdělendovizuálníchsekcí na hlavní stránce. Každý produkt obsahuje kvalitní náhledovýobrázek, kterýsedynamickyměnívzávislostina vybrané variantě. Místo zdlouhavého čtení textových popisků ve formulářích vybírá uživatel z velkých interaktivních prvků. Například velikosti jsou řešeny jako jasně viditelná a snadno klikatelná (tzv. touch-friendly) tlačítka. Barvy pak nejsou ukryté v nepřehledném roletovém menu (dropdown listu), ale jsou prezentovány formou vizuálních interaktivních teček, které reprezentují reálný odstín látky. Uživatel tak na první pohled a intuitivně vidí, jakou variantu si přesně zvolil.

Tento přístup dramaticky snižuje chybovost na straně uživatele,neboťokamžitávizuálnízpětnávazba(změna hlavní fotografie mikiny na červenou ihned po kliknutí na červenou tečku) vylučuje pochybnosti o správnosti volby.

### 3.2 Proces objednávání a košík

Samotný objednávkový proces byl navržen tak, aby minimalizoval tření a tzv. opuštěné košíky. Student si můžedosvéhovirtuálníhokošíkuvložitlibovolnýpočet produktů. Jakmile se zákazník rozhodne objednávku dokončit, pouze se přihlásí přes svůj školní účet, díky čemuž mu aplikace ušetří několik vteřin vyplňování různých údajů.

### 3.3 Rozhraní pro administrátory a proces výdeje

Neméně důležitou a často opomíjenou součástí UX byl návrh grafického rozhraní pro samotné správce systému (administrátory). Administrátorské rozhraní poskytuje centrální přehled nad všemi aktuálními i historickými dávkami a agreguje počty objednaných kusů v reálném čase. Administrátor na první pohled vidí, zda konkrétní barva v dané dávce splnila kritérium minimálního počtu kusů pro tiskárnu.

Zásadní proměnou prošel i kritický proces samotného výdeje oblečení. Místo dřívějšího zdlouhavého hledání jmen v dlouhých papírových seznamech vytištěných z Excelu nyní administrátor jednoduše naskenuje QR kód objednávky, který ukáže student, nebo vyhledá studenta v systému a jedním kliknutím přepne stav jeho objednávky na „Vyzvednuto“. Tímto krokem se objednávka nejen zařadí do archivu, ale zároveň systém automaticky odešle studentovi poděkování a potvrzení o převzetí. Výdej je tak výrazně rychlejší a prakticky se tím eliminuje prostor pro lidskou chybu, ke které v minulosti docházelo vlivem nepozornosti při odškrtávání fixou na papíře.

### 4. Architektura a Implementace

Z technologického hlediska byla aplikace navržena tak, aby poskytovala velmi rychlou odezvu pro uživatele a zároveň byla snadno a levně udržovatelná do budoucna. Byla koncipována jako moderní webová aplikace využívající aktuální webové standardy a bezpečnostní postupy.

### 4.1 Technologický stack: SvelteKit a Svelte 5

Jako hlavní a jediný framework pro vývoj frontendové i backendové části byl zvolen SvelteKit, poháněný nejnovější verzí knihovny Svelte 5.

### Obrázek 3. Administrátorská správa stavů objednávky

Volba SvelteKitu byla do značné míry motivována jeho architektonickým přístupem. Na rozdíl od jiných populárních nástrojů (jako je například React nebo Vue) přesouvá Svelte podstatnou část práce do fáze kompilace (build-time). Místo toho, aby do prohlížeče posílal těžkou knihovnu pro správu takzvaného virtuálního DOMu(DocumentObjectModel),kompilujeSveltekomponentydovysoceoptimalizovanéhoačistéhoJavaScriptu. Výsledkemjeextrémněrychléuživatelskérozhranísminimální paměťovou náročností, které běží plynule i na starších mobilních zařízeních s horším internetovým připojením (například ve školních budovách se slabým signálem).

Nasazení Svelte 5 navíc umožnilo plné využití nového systému reaktivity, takzvaných Runes (např. makra $state a $derived). Tento systém nahrazuje starší a často matoucí koncepty reaktivity vázané na lokální proměnné, čímž činí kód robustnějším, snáze čitelným a méně náchylným na chyby při rozšiřování funkcionality.

Pro definici vizuálního stylu aplikace nebyl záměrně použit žádný předpřipravený CSS framework. Vzhled je plnědefinovánzapomocičistéhokaskádovéhostylování (Vanilla CSS) umístěného přímo v rámci Svelte komponent. Aby byla zajištěna vizuální konzistence, využívá aplikace robustní systém CSS proměnných (CSS variables) definovaných na globální úrovni, které definují paletubarev(např. –color-surface,–color-brand-main) a rozměry napříč celou aplikací.

### Obrázek 4. Logo frameworku Sveltekit

### 4.2 Správa dat a integrace Drizzle ORM

Aby byla zajištěna dlouhodobá bezpečnost a perzistentní uložení všech strukturovaných dat, využívá aplikace výkonnou relační databázi PostgreSQL. Pro komunikaci s touto databází v prostředí Node.js byl implementován moderní nástroj Drizzle ORM (ObjectRelational Mapping).

Drizzle ORM poskytuje přísnou typovou kontrolu díky hluboké integraci s jazykem TypeScript. Databázové schéma je modulárně definováno přímo v kódu repozitáře a rozděleno do přehledných logických bloků obsahujících entity pro Produkty, jejich Varianty (kombinace barev a velikostí), jednotlivé uživatelské Objednávky a hromadné Dávky (Batches).

Díkytomutostriktnímudefinováníschématujezajištěno, žeseaplikacevyhneneočekávanýmpádůmzpůsobeným nekonzistencí dat – vývojář má již během psaní kódu jistotu, s jakými datovými typy pracuje. Pro rychlé iterace a zavádění nových funkcí aplikace hojně využívá inástrojeproautomatickégenerováníaaplikacidatabázových migrací zprostředkovaných přes CLI nástroj drizzle-kit.

### 4.3 Autentizace a Bezpečnost

Ochrana soukromí studentů a bezpečnost dat byly prioritou od samého počátku návrhu architektury. Pro správuidentit,přístupovýchprávapřihlašovánívyužívá projekt knihovnu better-auth.

Komunikacesdatabázíaveškerácitliváobchodnílogika (jakojepřesouváníobjednávekmezistavy,čtenícitlivých osobních údajů ze zadaných formulářů) probíhá výhradně v bezpečném prostředí na straně serveru. Koncovému uživateli se do prohlížeče dostanou striktně pouze ta data, na která má oprávnění. Administrátorské funkce, jako je například mazání objednávek či uzavíránídávek, podléhajípřísnéabezpečnéserverové autentizaci.

### 4.4 Automatizace e-mailových notifikací

Jak již bylo zmíněno, jedním z hlavních cílů projektu bylo zajistit, aby student nezůstal po odeslání objednávky bez informací. Tento cíl byl naplněn implementací plně automatizovaného e-mailového modulu postaveného na knihovně Nodemailer.

Modul je integrován přímo do SvelteKitu do formy serverových webhooků. Kdykoliv se v relační databázi změní stav konkrétní objednávky administrátorským zásahem, systém tuto událost na pozadí asynchronně zachytí, vygeneruje úhledně naformátovaný HTML notifikační e-mail obsahující logo školy a aktuální zprávu prostudenta,anáslednějejodešlepomocínastaveného SMTP (Simple Mail Transfer Protocol) serveru. Celý proces notifikací tak funguje naprosto bezúdržbově.

### Obrázek 5. Emailové upozornění o změnu stavu objednávky

### 4.5 Nasazení a DevOps infrastruktura

Zpohledukoncovéhonasazení(deployment)jeprojekt postaven tak, aby byl snadno provozovatelný na běžné serverové infrastruktuře. Využívá k tomu technologii kontejnerizace pomocí platformy Docker. Aplikace je zabalena do malého, výkonného Linuxového obrazu s instalovaným prostředím Node.js a spolu s databází běží orchestrovaně prostřednictvím docker-compose.

Tento způsob nasazení (DevOps praxe) zajišťuje izolovanostběhu,snadnézálohováníapředevšímpřenositelnostsystému,pokudbyvbudoucnuškolaměnilaposkytovatelehostingu neboby seprojektreplikoval na jinou vzdělávací instituci.

### 5. Testování použitelnosti

Žádný softwarový produkt nelze považovat za úspěšný, dokudneníplněověřenjehoskutečnýmiuživateli. Kověření

toho, zda nově vzniklý systém skutečně řeší původně definované problémy a poskytuje plynulý uživatelský zážitek, bylo provedeno strukturované uživatelské testovánípoužitelnosti. Testováníproběhlonareprezentativním vzorku 29 respondentů z řad studentů gymnázia.

### 5.1 Metodika a realizace testování

Testování probíhalo formou průchodu přesně definovanými scénáři. Účastníci dostali testovací protokol s úkoly, které pokrývaly celý životní cyklus používání aplikace – od základní orientace na stránce, přes výběr zboží a registraci, až po sledování stavu objednávky a její virtuální vyzvednutí.

Po dokončení praktické části vyplňovali respondenti dotazník, kde hodnotili jednotlivé kroky i celkový dojem z aplikace na standardní školní škále od 1 (nejlepší) do 5 (nejhorší). Nechyběl ani prostor pro kvalitativní textovou zpětnou vazbu, hlášení chyb a návrhy na zlepšení.

### 5.2 Celkové hodnocení a silné stránky

Celkovépřijetíaplikacebylomimořádněpozitivní. Drtivá většinarespondentů(26z29)ohodnotilaaplikacivýslednou známkou 1. Pouze jeden tester udělil známku 2 a dva testeři hodnotili známkou 3.

V textových odpovědích testeři nejčastěji chválili čistý a přehledný design, celkovou vizuální úroveň e-shopu a jednoduchost používání. Kladně byla hodnocena také celková rychlost aplikace (což potvrzuje správnou volbu frameworku SvelteKit) a přítomnost kvalitních produktových fotografií. Z hlediska funkcionality uživatelé velmi oceňovali přehlednost v detailu své objednávky a možnost ji v případě omylu snadno zrušit.

### 5.3 Analýza scénářů a odhalené nedostatky

Nejcennějšímvýstupemtestovánívšaknebylypochvaly, ale identifikace reálných UX a technických problémů, nakteréuživateléběhemprůchodudevítiscénářinarazili.

Scénář 1 a 2: Orientace a výběr produktů Zatímco samotné seznámení s katalogem, filtrování produktů a jejich vyhledávání (Scénář 2) fungovalo u všech respondentů naprosto bezchybně a intuitivně (převaha známek 1), ve Scénáři 1 se objevil specifický problém. Tímbylaresponzivitanamobilníchzařízeních –navigačnílišta(navbar)sefektemrozostřenéhopozadí (blur) měla v určitých situacích špatný kontrast textu, kvůli čemuž jeden z uživatelů přehlédl tlačítko pro přihlášení.

Scénář 3: Registrace a přihlášení Tento testovací krok proběhl u všech testerů hladce a bez jakýchkoliv technických chyb či záseků. Uživatelské toky byly navrženy srozumitelně a respondenti hodnotili proces známkami 1 a 2.

Scénář 4 a 5: Pokladna a Detail objednávky Práce s košíkem (úprava množství, mazání) a samotný průchodpokladnou(checkout)seukázalyjakonaprosto intuitivní a bezproblémové. Detail objednávky byl hodnocen jako jedna z nejlepších funkcí aplikace, informace byly srozumitelné a kompletní (26x známka 1).

Scénář 6 a 7: Změny a Sledování stavu Úpravy existujících objednávek ze strany uživatele i jejich změna (Scénář 6) proběhly bez chyb. V případě sledovánístavuobjednávky(Scénář7)uživatelévdotazníku upozorňovalinanutnostmanuálníhoobnovení(refreshe) stránky, aby se jim propsala změna stavu od administrátora.

### 6. Implementovaná vylepšení a opravy

Nazákladěvýšezmíněnéhotestováníbylvytvořenakční plán oprav. Drtivá většina chyb a UX nedostatků nahlášenýchuživateliběhemtestováníbylabezprostředně opravena a nasazena do produkce, aby byla aplikace plně připravena na ostrý provoz:

- Rozšíření administrátorských funkcí: Z přímé
zpětnévazbyodadministrátorůpotestovánívzešel
požadavek na možnost nejen upravovat stávající
položky v objednávce, ale také do již vytvořené
objednávkypřidatzcelanovýprodukt. Tatoužitečná
funkce byla obratem naprogramována a implementována do administračního rozhraní.
- Mobilní optimalizace a UI: Byl upraven kontrast
textu v navigaci nad rozostřeným pozadím tak,
abytextnesplývalanavigačníprvky(včetnětlačítka
pro přihlášení) byly perfektně čitelné na všech
mobilních zařízeních.
- Real-time aktualizace (vyhodnoceno a zamítnuto): Připomínka ohledně nutnosti refreshe
při sledování stavu objednávky (Scénář 7) byla
pečlivě vyhodnocena. Pro tento typ aplikace je
však zavádění live-updates (např. pomocí WebSockets)technologický„overkill“,kterýbyzbytečně
komplikovalarchitekturu. Notifikacejsouprimárně
řešeny spolehlivě přes e-mail, proto byl tento
požadavek z technologického hlediska zamítnut.

### 7. Závěr

Projekt webové aplikace pro správu a distribuci školníchpropagačníchpředmětůsloužíjakovynikajícíavpraxi

ověřený případ toho, jak může i v na první pohled konzervativnímprostředístředníškolykvalitněapromyšleně navržená digitalizace razantně zefektivnit zavedené, ovšem historicky zastaralé a vyčerpávající procesy. Nahrazením nepřehledných formulářů moderní webovou aplikací, která je šitá na míru specifickým potřebám prodeje školního oblečení v tzv. batch modelu, se podařilo dosáhnout výborných výsledků.

Nejenžesepovedloradikálnězlepšituživatelskýzážitek při samotném nákupu, ale současně se prakticky eliminovalalidskáchybovostnastraněadministrátorů. Zásadním benefitem aplikace je její transparentnost – studenti mají konečně přehled o svých objednávkách a administrátoři z řad pedagogů i studentské rady mohou věnovat ušetřené desítky hodin užitečnější činnosti.

Proběhlé uživatelské testování navíc potvrdilo, že aplikace po vizuální a funkční stránce obstála na jedničku. Zpětnávazbaod29reálnýchuživatelůpomohlaodhalit skryté nedostatky (jako je ztráta košíku po registraci či chybějící potvrzovací notifikace) ještě před ostrým startem.

Díkynasazenínejmodernějšíchtechnologiísoučasného webového vývoje, konkrétně frameworku SvelteKit doplněného o robustní databázi PostgreSQL s přístupem přesDrizzleORMazajištěnéhokontejnerizacívDockeru, vzniklo škálovatelné řešení. To škole nedává jen jednorázový produkt k maturitě, ale naopak buduje silný technologický základ s velkým potenciálem pro budoucí inovace. Tento projekt tak představuje perfektní ukázku úspěšného propojení teoretických poznatků z oblasti návrhu uživatelských rozhraní, softwarového inženýrstvíatestovánípoužitelnostipřiřešeníreálného problému z praxe.

### Poděkování

Závěrem bych chtěl poděkovat Mgr. Aleši Novákovi za odbornou pomoc při integraci přihlašování pomocí školníchMicrosoftúčtů. VelkédíkypatřítakéMgr. Ondřeji Láskovi,kterýsezhostilroleklientavelmiprofesionálně. Oceňujipředevšímjehoaktivnízájemoprojekt,pravidelné konzultace na úrovni klienta a zpracovatele i poskytování věcné zpětné vazby. V neposlední řadě děkuji vedoucímu práce, Ing. Adamu Ferenczovi, za vedení a možnost konzultovat otázky ohledně projektu.