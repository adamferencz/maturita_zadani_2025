Maturitní projekt - Gymnázium Havlíčkův Brod - 2026 Project Manager: návrh a implementace systému pro řízení projektu v malé firmě

Jiri Kotlas

Abstrakt Tento článek popisuje návrh, implementaci a vyhodnocení webového informačního systému Project Manager určeného pro malé firmy. Cílem práce bylo sjednotit řízení zakázek, dokumentů a přístupových práv do jednoho nástroje, který pokrývá životní cyklus obchodního případu od nabídky po fakturaci a firmě poskytuje centrální místo pro rychlé zjištění stavu zakázky, odpovědných osob i navazujících dokumentů. Implementace je postavena na Symfony 7.4, PHP 8.3, PostgreSQL 15, Twig a Bootstrap 5. Článek zahrnuje analýzu požadavků, porovnání alternativních řešení (Caflou, Raynet, Lamael), návrh architektury a databázového schématu, implementaci serverové i klientské části, testování i nasazení. Výsledky ukazují, že navržené řešení pokrývá klíčové potřeby malé firmy v oblasti procesního toku dokumentů, řízení oprávnění (ACL, Access Control List) a operativního vykazování.

Gymnazium Havlickuv Brod

### 1. Úvod – problematika řízení projektů v malých firmách

Malé firmy typicky fungují v prostředí omezených kapacit. Jedna osoba často zastává více rolí současně: obchod, koordinaci realizace, komunikaci s klientem i administrativu. Tato realita vytváří tlak na jednoduché, ale spolehlivé procesy. V praxi se však projektová agenda často spravuje kombinací tabulek, e-mailů, cloudových úložišť a účetních systémů, které spolu nejsou konzistentně propojené. Na začátku podnikání může takový model vyhovovat, ale s rostoucím počtem zakázek rychle přestává stačit. Lidé pak obtížně dohledávají, která verze dokumentu je správná, kdo má co dokončit a v jaké fázi se zakázka skutečně nachází.

Typický problém není jen v tom, že data jsou na více místech, ale hlavně v tom, že mezi nimi chybí jasné propojení. Obchodní nabídka, objednávka, smlouva, akceptační protokol a faktura bývají ukládané odděleně, často s různým názvoslovím a bez jednotné identifikace. V praxi to znamená, že stejná zakázka se v různých souborech „tváří“ jako něco jiného. Pak je obtížné rychle odpovědět na základní provozní otázky: co je aktuální verze, kdo s tím může pracovat a jestli čísla v přehledech odpovídají realitě.

Systém Project Manager byl navržen jako přímá odpověď na uvedené problémy. Cílem nebylo vytvořit univerzální platformu pro všechny firmy, ale praktický informační systém pro konkrétní provozní scénář malé firmy. Hlavní myšlenka je jednoduchá: mít klíčové procesy na jednom místě, mít jasně určené role a mít data, kterým může vedení při rozhodování důvěřovat.

### 2. Analýza požadavků – výsledky konzultací s firmou

Analýza vycházela z konzultací se zástupci firmy a z revize běžných provozních postupů. V první fázi byl sestaven seznam činností, které firma vykonává opakovaně. Ve druhé fázi byly scénáře ověřeny na prototypu obrazovek a formulářů. Tento iterativní přístup byl zvolen proto, že uživatelé často přesněji definují potřeby až při práci nad konkrétním návrhem.

### 2.1 Metodika sběru a prioritizace

Požadavky byly průběžně tříděny metodou Must-have, Should-have a Could-have (kritické, důležité a volitelné požadavky). Do kategorie Must-have spadalo projektové členění dat, dokumentové moduly, role a omezení přístupu a základní vykazování. Kategorie Should-have zahrnovala profil uživatele, změnu hesla,

reset hesla a komfortnější práci v tabulkách. Do kategorie Could-have byly zařazeny prvky jako pokročilý monitoring, formalizované CI/CD (continuous integration/continuous delivery, průběžná integrace a doručování změn) a rozšířená API vrstva (aplikační programové rozhraní). Tento způsob prioritizace umožnil udržet realistický rozsah implementace a současně dodat systém využitelný v běžném provozu.

### 2.2 Funkční požadavky

V rámci analýzy byly identifikovány funkční požadavky pokrývající celý provozní cyklus firmy. Patří sem evidence klientů včetně identifikačních údajů a kontaktů, evidence projektů navázaných na klienta a přiřazení uživatelů k projektům s rolí a aktivním stavem přiřazení. Dále sem patří správa dokumentových modulů (nabídky, objednávky, smlouvy, akceptační protokoly a faktury), řízení stavového toku přes číselníky, bezpečný upload/download dokumentů s kontrolou oprávnění a přehledy s časovým filtrem. Praktický příklad: vedoucí projektu během několika kliknutí zjistí, zda je konkrétní zakázka stále ve fázi nabídky, nebo už je připravená k fakturaci.

Z konzultací vyplynul důležitý bezpečnostní detail: při přiřazení uživatele do projektu nestačí pouze klientský filtr aktivních účtů, ale je nutná i serverová pojistka proti ručně upravenému požadavku.

### 2.3 Nefunkční požadavky

Nefunkční požadavky reflektovaly provozní realitu malé firmy. Systém měl být webově dostupný v běžném prohlížeči, nasaditelný na Ubuntu VPS (virtuální privátní server), postavený nad PostgreSQL 15, vybavený role-based přístupovým modelem (přístup podle role uživatele) a navržený bez zbytečné architektonické složitosti.

Z hlediska kvality služby byly průběžně sledovány i atributy jako dostupnost v pracovní době, předvídatelná odezva u běžných CRUD operací (create, read, update, delete), auditovatelnost změn dokumentů a jednoduchá obnova po provozní chybě. Tyto atributy nebyly formalizovány jako samostatné SLA metriky (service level agreement, úroveň garantované služby), ale sloužily jako rozhodovací kritérium při návrhu architektury i deployment postupů.

### 2.4 Use-case scénáře jako validační rámec

Kověřeníúplnostipožadavkůbylydefinoványreprezentativní provozní scénáře. Obchodník vytvoří nabídku a předá ji do realizace. Projektový manažer přidá členy týmu a sleduje stav dokumentů. Administrátor

ověří přístupová práva a řeší výjimky v přidělení rolí. Management dohlédne fakturační stav v reportech. Tento postup pomohl zkontrolovat, že systém není navržen jen „na papíře“, ale odpovídá skutečné práci jednotlivých rolí.

Pro každý scénář byly vyhodnoceny tři parametry: počet kroků, riziko chybného vstupu a dohledatelnost výsledku. Tento přístup pomohl odhalit slabá místa už při návrhu formulářů a rout.

V analytické fázi se jako nejdůležitější ukázalo oddělit třiúrovněpožadavků: obchodní, procesníatechnickou. Obchodníúroveňříká, jakédokumentyfirmapotřebuje a jak rychle je musí umět dohledat. Procesní úroveň určuje, kdo co dělá a v jakém pořadí na sebe kroky navazují. Technická úroveň řeší, aby se data nerozpadala, aby bylo dohledatelné, kdo co změnil, a aby byly soubory bezpečně uložené. Teprve spojení těchto tří pohledů vedlo k návrhu, který je použitelný dnes a zároveň udržitelný do budoucna.

Součástí analýzy byla i identifikace chyb, které se v původním provozu opakovaly nejčastěji. Typicky šlo o neplatné verze dokumentů v oběhu, nejasné vlastnictví úkolů, duplicity klientských záznamů a obtížné dohledávání stavu zakázky při předání mezi rolemi. Tyto chyby nebyly způsobeny jedním systémovým selháním, ale kombinací nejednotných postupů a chybějícího centrálního datového modelu. Navržené řešení proto klade důraz na jednotný referenční bod dat a jasně definované odpovědnosti už v návrhu entit a oprávnění.

### 3. Existující řešení – porovnání alternativ

V porovnání byla použita kritéria, která odpovídají reálnému rozhodování malé firmy. Hodnocen byl cenový model pro malý tým, podpora projektového procesu, podpora dokumentového toku od nabídky po fakturu, granularita oprávnění, vykazování a přehledy, API a integrační možnosti i celková vhodnost pro českou firmu se silným důrazem na dokladové procesy. Hodnocení tedy nesledovalo pouze seznam funkcí, ale také míru praktické použitelnosti v každodenním provozu.

Caflou cílí na malé a střední firmy, které chtějí mít na jednom místě obchod, projekty, úkoly i finance. Silnou stránkou je šíře funkcí a rychlé nasazení bez vlastního vývoje. Limitem je, že firma musí přijmout předem daný datový model a workflow. Pokud má specifický dokumentový tok nebo neobvyklá oprávnění, často končí u kompromisů.

Raynet je silný především v CRM části (obchodní příležitosti, kontakty, pipeline a obchodní řízení). Pro firmy

orientované na obchod je to výhoda, protože získají rychlý přehled o výkonu týmu. Slabší stránkou je menší důraz na interní procesní tok dokumentů od nabídky po fakturaci v jednom uzavřeném modelu. V praxi to může znamenat potřebu doplnit další nástroj nebo vlastní integrační vrstvu.

Lamael se profiluje jako české řešení pro menší firmy s důrazem na evidenci zakázek, dokumentů a provozní přehled. Výhodou je lokální kontext a orientace na firemní agendu blízkou české praxi. Omezení se projeví ve chvíli, kdy firma vyžaduje detailně vlastní pravidla oprávnění a specifickou business logiku nad projekty. V takové situaci může být nutné přizpůsobení, které není vždy triviální.

Z cenového pohledu je vhodné chápat veřejné tarify jednotlivých služeb jako orientační vstupní cenu, která se v praxi mění podle počtu uživatelů, zvoleného tarifu a modelu fakturace. Při konečném rozhodnutí je proto nutné ověřit aktuální ceníky a zohlednit i provozní náklady spojené s případným skládáním více nástrojů dohromady.

Z ekonomického pohledu je nutné hodnotit celkové náklady vlastnictví (TCO, Total Cost of Ownership). Do nich patří nejen provoz serveru, ale i vývoj, údržba, opravy a čas lidí, kteří systém dlouhodobě spravují. Vlastní řešení může být nákladově výhodné zejména tehdy, pokud má firma dostupnou interní technickou kapacitu a systém využívá dlouhodobě. Pokud firma interní vývojový tým nemá, může být SaaS varianta v řadě scénářů levnější a provozně jednodušší.

V návaznosti na analýzu požadavků i srovnání alternativ je v další kapitole představen návrh vlastního systému, který uvedené limity cíleně řeší.

### 4. Návrh systému – architektura a databázové schéma

### 4.1 Architektonický přístup

Aplikace je navržena jako server-side rendered monolit (SSR, vykreslování stránek na serveru). V praxi to znamená, že většina logiky je soustředěna v jedné aplikaci a uživatel dostává hotovou stránku ze serveru. Tok zpracování je: Prohlížeč →Apache (PHP runtime, tedy běhové prostředí) →Symfony Controller →Service/Repository →Doctrine ORM (objektově-relační mapování) →PostgreSQL. Volba monolitu byla vědomá: pro malý tým je obvykle důležitější stabilita, čitelnost a snadná údržba než složitá architektura rozdělená do mnoha služeb. Konkrétně to pomáhá třeba při opravě chyby, protože tým hledá problém v jednom projektu, ne ve více oddělených aplikacích.

Architektura je navržena tak, aby omezila skrytou složitost. Klientská vrstva obsahuje pouze tolik interaktivity, kolik je nutné pro pohodlnou práci se seznamy a filtry, zatímco hlavní obchodní pravidla zůstávají na serveru. Tímsesnižujerizikonekonzistentníhochování mezi obrazovkami a zároveň se usnadňuje testování. Záměrně nebyla zvolena oddělená SPA/API architektura (single-page application + samostatné aplikační rozhraní), protože by v počátečním rozsahu přinesla více provozní složitosti než praktického přínosu.

Obrázek 1. Architektura systému (klient, Apache/PHP, Symfony vrstvy, Doctrine, PostgreSQL, úložiště souborů).

Obr. 1 shrnuje klíčový návrh: jedna vstupní aplikace, centrální business logika a oddělené datové i souborové úložiště. Díky tomuto uspořádání je v praxi jasné, kde se vyhodnocuje autorizace, kde se aplikují validační pravidla a kde vzniká auditní stopa operací.

### 4.2 Modulární rozdělení

Doména je rozdělena do modulů uživatelé a role, klienti, projekty, dokumenty (nabídka, objednávka, smlouva, akceptační protokol, faktura) a vykazování. Každý modul má konzistentní strukturu controller– entity–repository–form–template, což zjednodušuje orientaci v kódu i budoucí rozšiřování.

### 4.3 Databázový návrh

Databázové jádro tvoří entita Projekt, na kterou navazují dokumentové entity i přístupová logika. Klient je ve vztahu 1:N k projektu. Projekt je ve vztahu M:N k uživatelům přes entitu ProjektUzivatel a současně ve vztahu 1:N k dokumentovým entitám Nabidka, Objednavka, Smlouva, AkceptacniProtokol a Faktura. Stavová logika je oddělena do samostatných status tabulek. Projekt v tomto návrhu funguje jako hlavní spojovací uzel, přes který se dohledá, kdo na zakázce pracuje a jaké dokumenty k ní patří.

Oddělení statusů do samostatných tabulek je výhodné pro dlouhodobou údržbu. Stav není volný text, ale

řízená hodnota s kódem a pořadím, což usnadňuje validaci i reportování.

### 4.4 Návrh proti datové nekonzistenci

Při modelování byly identifikovány tři kritické body nekonzistence: dokument bez projektu, uživatel s přístupem bez aktivního přiřazení a nesprávná posloupnost dat (například datum vystavení po datu splatnosti). Mitigace byla řešena kombinací cizích klíčů, aplikační validace a voter pravidel. Smyslem těchto kontrol je, aby systém nepřipustil chybu už při vzniku, ne až při pozdějším reportu.

### 4.5 Konzistence provozních a reportovacích dat

Návrh byl veden tak, aby stejné vazby sloužily pro provozní obrazovky i přehledy. Pokud je dokument navázán na projekt, stejná vazba se používá při autorizaci i agregaci metrik. Tím se snižuje riziko nesouladu mezi seznamy a přehledovou deskou.

### 5. Výběr technologií – zdůvodnění stacku

Technologická volba vychází z požadavků firmy a cíle projektu: mít systém, který je robustní, ale provozně jednoduchý.

### 5.1 Backend

Backend je postaven na Symfony 7.4, které poskytuje robustní aplikační strukturu a kvalitní bezpečnostní model. Runtime tvoří PHP 8.3 a databázová vrstva využívá Doctrine ORM s migracemi nad PostgreSQL 15, což umožňuje řízený vývoj schématu a vysokou datovou integritu. Praktický přínos je v tom, že změny databáze probíhají opakovatelně a kontrolovaně, takže je menší riziko rozbití prostředí při vývoji i nasazení.

Jako alternativa byl zvažován Laravel. Ten by umožnil rychlý start, ale vzhledem k požadavkům na jemnější ACL nad projektovým kontextem, existujícím zkušenostem se Symfony Security a potřebě dlouhodobé čitelnosti vrstev vycházelo Symfony vhodněji. Zvažována byla i Node.js architektura (NestJS/Express), která je silná pro API scénáře, ale pro SSR orientovaný informační systém by znamenala vyšší implementační i provozní složitost. Příklad praktického dopadu: každý další samostatný servis by znamenal další monitoring, konfiguraci a řešení komunikace mezi službami.

### 5.2 Frontend

Frontend je navržen jako SSR vrstva v Twig šablonách s Bootstrap 5. Interaktivitu zajišťují DataTables (knihovna pro tabulkové přehledy) pro práci se seznamy

a Stimulus (lehký JavaScriptový rámec) spolu s importmap/AssetMapper, což udržuje klientskou vrstvu lehkou bez složitého JavaScript toolchainu. Pro uživatele to znamená rychlejší orientaci v tabulkách a menší pravděpodobnost, že se rozhraní bude chovat nestabilně na slabším zařízení.

Alternativou byl SPA přístup (např. React nebo Vue). Ten by přinesl vyšší flexibilitu klienta, ale za cenu dodatečné API vrstvy, složitější autentizace mezi frontem a backendem a vyšší náročnosti deploymentu. V kontextu malého týmu vychází SSR přístup pragmaticky výhodněji.

### 5.3 Provoz

Z provozního pohledu je vývojové prostředí reprodukovatelnédíkyDockeruaDockerCompose. Aplikačníkontejner využívá image php:8.3-apache a databázový kontejner PostgreSQL 15. Volba sleduje cíl mít jednoduchý a předvídatelný provozní model bez zbytečných vrstev.

U databáze byla alternativou MySQL/MariaDB. PostgreSQL byla zvolena kvůli konzistenci práce s relačními vazbami, kvalitětransakčníhomodeluadobrépodpoře v Doctrine. V souhrnu tak volba stacku představuje kompromis mezi výkonem, udržitelností a nízkou provozní režií.

### 6. Vnitřní architektura systému

Tato kapitola vysvětluje, proč je architektura navržena právě tímto způsobem a co to přináší v každodenním provozu.

### 6.1 Základní princip: jedna business pravda, více technických vrstev

V systému existuje jedna business realita: klient, projekt, dokumenty, uživatelé a jejich role. Tato realita je rozložena do vrstev: databáze ukládá fakta, entity je mapují do objektů, repository je cíleně vyhledávají, formy validují vstup, controllery orchestrují scénář požadavek-odpověď a model vrstva sjednocuje společné chování napříč entitami.

Pokud by některá vrstva chyběla, systém by se rychle stal nepřehledným. Bez repository by filtrace skončila v controllerech, bez form vrstvy by validace nebyla konzistentní a bez modelového rozhraní by bylo složité sdílet ACL pravidla napříč dokumenty.

### 6.2 Databáze: proč je v ní to, co v ní je

Databáze není jen sklad dat, ale nositel obchodní logiky. Klient reprezentuje obchodního partnera,

projekt konkrétní zakázku a vazební tabulka ProjektUzivatel nese odpovědnostní kontext: kdo je k projektu přiřazen, v jaké roli a zda je přiřazení aktivní. Díky tomu lze například zpětně dohledat, proč konkrétní uživatel viděl určitý dokument a jiný ne.

Dokumentové entity nejsou sloučeny do jedné univerzální tabulky, ale drženy samostatně (nabídka, objednávka, smlouva, akceptační protokol, faktura), protože každá má jiná povinná pole a jiná doménová pravidla. Statusy jsou odděleny do číselníků, aby stav nebyl volný text.

### 6.3 Model vrstva a sdílená ACL logika

Rozhraní ProjectRelatedInterface definuje, že entita umí vrátit svůj projekt. Díky tomu se stejné přístupové pravidlo dá použít nad různými dokumenty bez znalosti interních detailů třídy.

### 6.4 Repository vrstva: proč nejsou dotazy v controlleru

Repository je místo, kde se řeší výběr dat. Například ProjektRepository koncentruje dotazy pro projektový seznam dle role. Fakturační repository drží metody pro neuhrazené a po splatnosti faktury i agregace tržeb pro report. Díky tomu zůstává controller čitelný a doménová pravidla mají jedno místo pravdy.

### 7. Implementace backendu – struktura, bezpečnost, validace

### 7.1 Struktura aplikační vrstvy

Projekt není navržen jako veřejné REST API, ale jako modulární webový backend. Klíčové moduly drží konzistentní CRUD tok a uživatel se napříč systémem pohybuje stejným mentálním modelem, takže podobné akce se v různých částech aplikace ovládají obdobně.

### 7.2 Bezpečnostní model

Bezpečnost je navržena jako vícevrstvý mechanismus: route-level ochrana v konfiguraci, role-level ochrana přes IsGranted a object-level ochrana přes Votery a denyAccessUnlessGranted. Prakticky to znamená, že selhání jedné kontroly automaticky neznamená průnik do systému. Role hierarchy je nastavena tak, že ROLE_MANAGEMENT dědí ROLE_USER a ROLE_ADMIN dědí obě nižší role.

Jemnozrnná autorizace je řešena přes ProjektVoter, ProjectAccessVoter a KlientVoter. Bezpečnostní model byl navržen tak, aby byl čitelný i při auditu: role určují

Obrázek 2. Vícevrstvý model autorizace (route, role, voter, entity).

obecný rozsah oprávnění, ale finální rozhodnutí nad konkrétní entitou dělá voter.

Model na obr. 2 odděluje hrubou kontrolu role od kontextového rozhodnutí nad konkrétním objektem. Uživatel může mít roli pro vstup do modulu, ale stále může být odmítnut, pokud není aktivně přiřazen k projektu nebo nemá právo na danou operaci. Právě tato druhá kontrola chrání systém před příliš širokým přístupem.

### 7.3 Bezpečnostní hrozby a mitigace

V návrhu byly explicitně zohledněny hrozby jako neoprávněný přístup k dokumentu přes ručně zadané URL, eskalace oprávnění přes manipulaci formulářového vstupu, nahrání nepovoleného typu souboru a únik citlivých dat přes veřejný upload adresář.

Mitigace zahrnují stahování dokumentů pouze přes controller s ACL kontrolou, backendové ověření přiřazení uživatele i při validním frontend vstupu, whitelist MIME typů (identifikace typu souboru) a limity velikosti souborů, plus ukládání souborů mimo veřejný webroot. Dokument je tedy vydán pouze při splnění oprávnění a systém současně kontroluje povolený obsah nahrávaných souborů.

### 7.4 Správa dokumentových souborů

Soubory jsou ukládány mimo veřejný webroot a metadata jsou držena v databázi. Stahování probíhá přes controller s ACL kontrolou, nikoliv přímým URL odkazem. To je zásadní bezpečnostní opatření, protože dokumenty obsahují obchodně citlivé informace.

### 8. Implementace frontendu – komponenty a UX

Na návrh a implementaci backendu navazuje klientská vrstva, která zachovává stejný princip nízké složitosti a dobré provozní udržovatelnosti. Cílem je, aby uživatelské prostředí bylo přehledné a zároveň nezvyšovalo technický dluh.

### 8.1 SSR přístup

FrontendpoužíváserverovýrenderingpřesTwig. Tento přístup je vhodný pro informační systémy, kde dominuje práce s formuláři, tabulkami a detailními přehledy. Výhodou je menší složitost klientské vrstvy a stabilní provoz na širším spektru zařízení.

### 8.2 Klíčové komponenty

Klíčové komponenty tvoří DataTables pro modulové seznamy a Stimulus controllery pro dílčí interakce. Pro vizualizaci reportovacích metrik je již využívána knihovna Chart.js a architektura zůstává otevřená i pro případné doplnění dalších specializovaných nástrojů. Importmap/AssetMapper umožnil provoz frontendu bez složité NPM build pipeline. Praktický přínos je, že úprava rozhraní nevyžaduje rozsáhlý build proces a vývojový cyklus zůstává rychlý.

### 8.3 UX principy a provozní použitelnost

Rozhraní je vedeno principy konzistence formulářů mezi moduly, předvídatelného umístění akcí, čitelných tabulek s filtrováním a role-based viditelnosti funkcí (zobrazení podle role). Uživatel se orientuje rychleji a systém nevyžaduje složité školení. Například uživatel v roli obchodníka nevidí administrátorské akce, které by pro něj byly matoucí, a může se soustředit jen na kroky relevantní pro svou práci.

### 9. Databázový design – ER, normalizace a optimalizace

### 9.1 Entitní model

Systém obsahuje 22 Doctrine entit. Kromě hlavních business objektů zahrnuje i dokumentové entity, statusové číselníky a entitu pro reset hesla. Databázové vztahy jsou explicitní a postavené na cizích klíčích.

ER pohled na obr. 3 vysvětluje, proč je středem modelu projekt. Většina praktických dotazů managementu i běžných uživatelů je vázána právě na projektový kontext.

### 9.2 Normalizační a integrační zásady

Vazební tabulka ProjektUzivatel obsahuje i provozní metadata (role v projektu, aktivita), což je klíčové pro ACL i auditní stopu. Status tabulky používají unikátní kódy a omezují riziko nekonzistence stavu.

Obrázek 3. ER diagram klíčových entit a vazeb.

### 9.3 Optimalizační přístup a evoluce schématu

Filtrování datasetu probíhá už na úrovni SQL dotazů (structured query language, jazyk pro práci s relační databází) podle role. Form query builder omezuje volitelné entity dle oprávnění. Doctrine migrations zajišťují opakovatelnost schématu napříč prostředími a snižují riziko divergence mezi vývojem a produkcí. Díky tomu se například nestane, že by testovací prostředí dovolilo uložit stav, který produkční databáze odmítne.

### 10. Testování – automatizace a uživatelské scénáře

Po implementaci datového modelu a aplikačních vrstev následovalo ověření funkčnosti a bezpečnosti systému na reprezentativních scénářích.

### 10.1 Automatizované testy

Projekt obsahuje funkční a servisní testy. Důležitým příkladem je test životního cyklu dokumentových souborů (nahrání/stažení/smazání), který ověřuje nejen logiku, ale i interakci mezi routou, oprávněním, databází a souborovým systémem. To je zásadní, protože chyba se často neobjeví v jedné vrstvě, ale až na jejich rozhraní.

### 10.2 Uživatelské testování

Byly ověřeny scénáře pro role admin, manager a user. Test report potvrzuje, že role vidí odpovídající množství dat, dashboardové agregace odpovídají databázi a běžný uživatel nemá přístup k cizím entitám. Pro

provoz to znamená, že systém už v této verzi drží základní bezpečnostní i datovou konzistenci.

Po nahrání fixtures bylo v databázi např. 19 uživatelů, 17 klientů, 38 projektů, 50 faktur, 47 nabídek, 11 objednávek a 10 smluv.

### 10.3 Metodické limity testování

Je korektní uvést, že pokrytí klasickými unit testy zatím není rozsáhlé. Část scénářů je validována manuálně a výkonová měření nebyla realizována jako samostatný benchmark. Limity jsou transparentní, ale nesnižují praktickou hodnotu ověření v cílovém provozním scénáři. Současně je důležité je otevřeně přiznat, aby bylo jasné, kde má navazovat další technický rozvoj.

### 11. Deployment – Docker, VPS a CI/CD zralost

### 11.1 Provozní varianty

AktuálníprovoznívariantajeDockerCompose. Nasazení využívá aplikační kontejner s runtime php:8.3-apache a samostatný databázový kontejner PostgreSQL 15. Tento model zajišťuje jednoduchou reprodukovatelnost prostředí mezi vývojem a produkcí. Reverse proxy vrstva (např. Nginx) může být doplněna později jako volitelný hardening krok, není však součástí současného provozního řešení.

Systém byl v rámci ověření nasazen také na testovací VPS od společnosti Forpsi, kde proběhlo pilotní testování reálnými uživateli ze zadavatelské firmy Bison v podmínkách blízkých běžnému provozu. Tato fáze potvrdila funkčnost hlavních modulů, ale zároveň odkryla řadu drobných nedostatků, které by se při čistě interním testu objevily obtížněji. Na základě zpětné vazby byla sjednocena prezentace formulářů a klíčových UI prvků (včetně konzistentních velikostí tlačítek), rozšířena práce s tabulkami tak, aby nabízely více praktických funkcí a byly uživatelsky přívětivější, a současně byly doladěny vazby mezi soubory v dokumentovém toku. Nasazení na testovací VPS tak nesloužilo jen jako technická verifikace deploymentu, ale i jako důležitý validační krok pro praktickou použitelnost systému v reálné firemní agendě.

### 11.2 Deploy skript

Skript deploy.sh zahrnuje aktualizaci kódu, instalaci produkčních závislostí, databázové migrace, seed status dat, cache clear/warmup, kompilaci assetů a reload webových služeb. Výhodou je jednoduchost a transparentnost kroků, limitem je absence automatického transakčního návratu při neúspěšném průběhu

Obrázek 4. Deployment schéma (Docker Compose: app/php:8.3-apache + db/postgres:15 + persistent volume).

nasazení. Pro menší tým je ale důležité, že celý postup je čitelný a dá se rychle zkontrolovat.

Obr. 4 vizualizuje provozní životní cyklus nasazení: update kódu, instalace závislostí, migrace schématu, příprava cache a restart služeb. Důležitým prvkem je oddělení stavu aplikace od stavu dat.

### 11.3 Návrh dalšího zlepšení CI/CD

Minimální doporučený posun zahrnuje automatické testy před nasazením, základní funkční test po nasazení, verzovaná vydání a návrat na poslední stabilní verzi.

### 11.4 Provozní observabilita

Doporučený posun je doplnit kontrolní endpoint dostupnosti, základní metriky (latence, chybovost, počet požadavků) a centralizaci logů. I jednoduchá provozní observabilita výrazně zkrátí dobu diagnostiky incidentu. V praxi to znamená, že tým rychleji rozliší, zda je problém v aplikaci, databázi, nebo infrastruktuře.

### 12. Výsledky – metriky a přínos pro firmu

Úspěšné nasazení systému umožnilo vyhodnotit praktické přínosy v reálném provozním prostředí.

### 12.1 Funkční výsledky

V aktuální verzi systém pokrývá kompletní hlavní tok agendy: klienty a projekty, dokumentové workflow od nabídky po fakturu, role-based ACL, dashboard a reporty i profil uživatele se resetem hesla. To odpovídá původnímu cíli dodat nástroj použitelný pro každodenní firemní provoz, ne jen demonstraci technologií.

### 12.2 Praktický dopad

Hlavním přínosem je centralizace informací a snížení provozní entropie. Tým pracuje s jednotným modelem

Obrázek 5. Ukázka dashboardu a reportovacích metrik.

dat, což zrychluje dohledání stavu zakázky a snižuje počet chyb při předávání práce mezi rolemi. V běžném provozu se to projevuje menším počtem nejasností a rychlejší reakcí na změny.

Výsledky z dashboardu (obr. 5) potvrzují, že centralizace dat není pouze technické zjednodušení, ale má okamžitý provozní efekt. Uživatel má v jednom pohledu přehled o rozpracovanosti, finančních ukazatelích i stavu dokumentů.

### 12.3 Kvantitativní indikátory přínosu

Ačkoli cílem nebyla formalizovaná ekonometrická studie, je možné sledovat měřitelné indikátory: čas dohledání stavu zakázky, počet chyb způsobených prací s neaktuálním dokumentem, rychlost kontroly přístupových práv a konzistenci reportovaných dat. Jde o ukazatele, které vedení firmy dokáže průběžně vyhodnocovat i bez složité analytiky. Orientační interní odhad z pilotního provozu ukázal, že čas dohledání stavu jedné zakázky se zkrátil přibližně z 20–40 minut (hledání v e-mailech a více souborech) na 3–8 minut v jednotném systému. Současně se podle provozních záznamů snížil počet případů práce s neaktuální verzí dokumentu přibližně o 40 – 60 % oproti stavu před nasazením.

### 13. Diskuse – limity a jejich řešení

### 13.1 Granularita oprávnění a konzistence workflow

Návrh ACL byl jednou z nejtěžších částí implementace. Voter přístup se ukázal jako udržitelný díky centralizaci pravidel. Oddělené status entity jsou robustnější než volný textový stav a zlepšují čitelnost reportu.

### 13.2 Testovatelnost a technický dluh

Ačkoli projekt obsahuje funkční testovací základ, rozsah unit/integration testů je zatím omezený. To v praxi znamená, že část jistoty je stále založena na

manuálním ověření. Budoucí rozvoj by proto měl mířit na vyšší pokrytí servisní a doménové logiky.

### 13.3 Validita a přenositelnost výsledků

Výsledky byly ověřeny na konkrétním firemním scénáři. Přenositelnost do jiných odvětví je reálná, ale vyžadovala by úpravu stavových číselníků, KPI (key performance indicators, klíčové ukazatele výkonnosti) a formulářových atributů. Komparace alternativ je vhodná pro strategické srovnání, ale nenahrazuje pilotní implementaci každého nástroje.

Dalším limitem je, že komparace alternativ vychází z veřejně dostupných produktových informací. Ty jsou vhodné pro orientační strategické srovnání, ale nenahrazují pilotní implementaci každého nástroje v identickém firemním prostředí.

### 13.4 Diskuse trade-offu

Vývoj vlastního řešení přináší kontrolu nad procesem, ale současně vyžaduje interní odpovědnost za údržbu a další rozvoj. Oproti SaaS nástrojům firma získává vyšší flexibilitu v doménovém modelu, ale nese i vyšší technické závazky. Jinak řečeno: větší svoboda je vykoupena větší dlouhodobou péčí o systém.

### 14. Praktický scénář provozu systému

### 14.1 Fáze 1 – vytvoření obchodního případu

Proces začíná založením klienta a projektu. Následně se provedou přiřazení uživatelů přes ProjektUzivatel včetně role a aktivního stavu. Tato data později přímo ovlivňují ACL i reporty.

### 14.2 Fáze 2 – dokumentový tok

Obchodník vytvoří nabídku, po jejím přijetí vzniká objednávka, následuje smlouva, po realizaci akceptační protokol a na jeho základě faktura. Celý tok je veden v jedné doménové databázi, proto je možné okamžitě dohledat návaznost dokumentů i jejich stav.

### 14.3 Fáze 3 – kontrola a rozhodování

Management používá dashboard a reporty pro operativníkontrolu. Kdispozicijsoupřehledyaktivníchdokumentů, nezaplacených faktur a stavu zakázek v čase. Klíčová je konzistence dat: report vychází ze stejného modelu jako provozní moduly. Díky tomu nevzniká situace, kdy by report ukazoval něco jiného než detail konkrétní zakázky.

### 15. Plán dalšího rozvoje

### 15.1 Stabilita, kvalita a UX/UI

Další rozvoj je veden snahou zachovat provozní stabilitu a současně zlepšit každodenní použitelnost systému. Prioritou je rozšířit unit a integration testy a zavést automatizované základní funkční testy po nasazení. Souběžně bude probíhat systematické doladění UX a UI (uživatelská zkušenost a uživatelské rozhraní): sjednocení chování formulářů napříč moduly, čitelnější validační hlášky, lepší orientace v akcích na detailu dokumentů a vyšší přehlednost tabulek na menších obrazovkách. Cílem je, aby aplikace zůstala rychlá a srozumitelná i při růstu počtu uživatelů a rozsahu dat. Praktický příklad: stejný typ validační chyby se bude zobrazovat stejným způsobem ve všech modulech, takže uživatel okamžitě ví, jak ji opravit.

### 15.2 API vrstva a integrace

Výraznou oblast dalšího rozvoje představuje formalizace API vrstvy (aplikačního programového rozhraní) pro bezpečnou integraci s dalšími firemními nástroji. Rozhraní má pokrýt zejména projekty, dokumentový tok a vykazování, aby bylo možné systém jednoduše propojit s účetními nebo analytickými službami. Klíčová je stabilita rozhraní, průběžná dokumentace a jasná pravidla autorizace přístupu třetích stran, protože bez nich by integrace rychle vedly k technickému dluhu. V praxi to znamená, že například účetní systém přečte faktury stejným způsobem i po budoucích aktualizacích aplikace.

### 15.3 Automatizace dokumentových toků a PDF

Velký praktický přínos má mít automatické vytváření PDF dokumentů přímo z formulářových dat. Tato funkcionalita má omezit ruční přepisy a sjednotit výstupy pro nabídky, objednávky, smlouvy i faktury. Současně je plánováno i obrácené zpracování, tedy načítání dat z přijatých PDF zpět do systému, aby bylo možné urychlit administrativní tok při přepisu externích podkladů. U kritických dokumentů zůstane zachována finální kontrola uživatelem před odesláním.

### 15.4 Auditovatelnost změn a provozní transparentnost

V návaznosti na bezpečnostní model bude posílena auditní stopa tak, aby bylo jednoznačně dohledatelné, kdo, co a kdy upravil. Evidován nebude jen samotný typ operace, ale i kontext změny nad konkrétní entitou a možnost rychlého porovnání původního a nového stavu u vybraných klíčových polí. Tento přístup sníží

riziko nejasností při předání agendy mezi rolemi a zároveň usnadní interní kontrolu i zpětnou analýzu incidentu.

### 15.5 AI podpora rozhodování nad interními daty

Perspektivní směr představuje využití interních historických dat pro AI predikci výkonnosti firmy. Predikční modely mohou v budoucnu podpořit odhad vytíženosti, rizika zpoždění zakázek nebo pravděpodobného vývoje finančních ukazatelů a včas identifikovat problémové trendy. Tato část bude rozvíjena postupně a s důrazem na validaci výstupů, aby AI sloužila jako podpora rozhodování managementu, nikoli jako netransparentní automatické rozhodování bez lidské kontroly.

### 15.6 Produktizace pro více firem a modulární růst

Pokud se provozně potvrdí stabilita jádra systému, může být řešení nabízeno i dalším firmám s podobným procesním modelem. Tento krok předpokládá modulární rozvoj, kdy společné jádro zůstane jednotné a nové funkce budou vznikat jako oddělené moduly podle potřeb konkrétního segmentu nebo zákazníka. Takový přístup umožní škálovat produkt bez narušení už fungujících částí aplikace.

### 15.7 Governance a řízení změn

Rozvoj bude řízen lehkým, ale důsledným change managementem: každý požadavek bude popsán jako uživatelský scénář, doplněn o akceptační kritérium a po nasazení vyhodnocen z hlediska dopadu na provoz, UX i datovou konzistenci. Tím se sníží riziko nekoordinovaných změn a zachová se dlouhodobá udržitelnost systému i při růstu počtu modulů. Praktický přínos je, že i menší úpravy budou mít jasně určený cíl a způsob ověření.

### 16. Závěr

Cíl projektu, tedy navrhnout a implementovat systém prakticky použitelný v malé firmě, byl splněn. Projekt ukázal, že dobře navržená monolitická SSR aplikace může přinést vysokou provozní hodnotu: nízkou složitost, srozumitelnouúdržbuapříménapojenínafiremní procesy.

Ve srovnání s obecnými SaaS nástroji je hlavní výhodou přesné přizpůsobení interním procesům firmy. Další rozvoj směřuje k technické stabilitě, vyšší uživatelské kvalitě, silnější auditovatelnosti změn, automatizaci dokumentových toků přes PDF a postupnému využití AI predikcí nad interními daty. Perspektivním směrem

je i možná produktizace systému pro více firem formou modulárních rozšíření. Hlavním přínosem práce není aplikace nejmodernějších, ale často složitých technologií, nýbrž dodání spolehlivého řešení, které firmě pomáhá eliminovat chyby, zrychlit rozhodování a udržet klíčová data pod kontrolou.

### 17. Doporučené přílohy

ER diagram domény (Klient, Projekt, ProjektUzivatel, dokumentové entity, status tabulky), architektonické schéma aplikačních vrstev, komparační shrnutí Caflou/Raynet/Lamael, snímek dashboardu a reportu a deployment diagram (VPS a Docker varianta).

### Poděkování

Děkuji vedoucímu práce za konzultace a vedení při návrhu i implementaci projektu.