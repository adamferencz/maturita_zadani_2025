Maturitní projekt - Gymnázium Havlíčkův Brod - 2026 Portál Kroužky Vysočina

Josef Holeček

Abstrakt Tato maturitní práce dokumentuje vývoj webového portálu „Kroužky Vysočina“, který slouží jako přehledný katalog volnočasových aktivit v Havlíčkově Brodě. Hlavním cílem projektu bylo vytvořit jednotné místo, které propojí rodiče a zájemce o kroužky s jejich organizátory a trenéry. Práce popisuje postup od prvotního nápadu a sběru požadavků až po vytvoření funkčního systému, který řeší problém roztříštěných informací na sociálních sítích a nástěnkách. Velký důraz je kladen na přehlednost prostředí a logické rozdělení uživatelských rolí, díky čemuž může běžný návštěvník snadno vyhledávat, zatímco trenéři a administrátoři mají nástroje pro efektivní správu nabízeného obsahu. V rámci realizace byl vytvořen systém umožňující kompletní správu životního cyklu kroužků, od jejich vložení přes schvalovací proces až po automatickou archivaci po skončení sezóny. Dokumentace se věnuje struktuře dat a návrhu uživatelského rozhraní, které je plně přizpůsobeno pro zobrazení na mobilních telefonech i počítačích. Výsledkem je prakticky použitelná aplikace nasazená do reálného provozu, která zjednodušuje orientaci v nabídce sportovních a vzdělávacích aktivit ve městě a nabízí stabilní základ pro případné budoucí doplňování o nové funkce, jako jsou rezervační systémy nebo mapové podklady.

Gymnázium Havlíčkův Brod

### 1. Úvod

Současná doba klade vysoké nároky na efektivitu vyhledávání informací, přičemž oblast volnočasových aktivit není výjimkou. V regionálním kontextu města Havlíčkův Brod však narážíme na výraznou informační roztříštěnost. Rodiče, kteří hledají vhodné vyžití pro své děti, nebo dospělí se zájmem o seberozvoj, jsou nuceni čerpat data z mnoha nesourodých zdrojů.

Aktuální stav lze charakterizovat jako decentralizovaný a nepřehledný. Hlavními informačními kanály jsou v současnosti:

- Sociální sítě: Zejména platforma Facebook, kde
jsou příspěvky o kroužcích rychle pohlceny algoritmem a po několika dnech se stávají prakticky
nedohledatelnými.
- Webové stránky jednotlivých klubů: Ty se liší
úrovní technického zpracování i aktuálností dat,
což znemožňuje rychlé srovnání parametrů, jako
je cena či věková kategorie.
- Tradiční média: Tištěné letáky v prostorách škol
a plakátovací plochy ve městě, které sice mají
lokální dopad, ale trpí absencí interaktivity a
obtížnou aktualizací v případě změn.

Tato fragmentace vede k situacím, kdy zájemce o aktivitu přehlédne nabídku, která by mu nejlépe vyhovovala, pouze z důvodu její špatné digitální viditelnosti. Trenéři a menší organizace v Havlíčkově Brodě zároveň postrádají jednotný prostor, kde by mohli svou činnost prezentovat bez nutnosti investovat do vlastních nákladných webových řešení.

Cílem tohoto projektu je proto vytvoření komplexního webového portálu „Kroužky Vysočina“. Tato platforma si klade za úkol sjednotit nabídku kroužků a profilů trenérů do jednoho uživatelsky přívětivého celku, usnadnit proces výběru pomocí pokročilého filtrování a poskytnout správcům i trenérům intuitivní nástroj pro správu obsahu v reálném čase.

### 2. Analýza požadavků a cílových skupin

Před zahájením samotného vývoje bylo nezbytné definovatklíčovéaktérysystémuajejichspecificképotřeby. Cílem analýzy bylo identifikovat problematická místa v procesu vyhledávání a nabízení kroužků a navrhnout funkce, které tyto bariéry eliminují.

### 2.1 Cílové skupiny a uživatelské role

Systém Kroužky Vysočina rozlišuje tři základní uživatelské úrovně, z nichž každá disponuje specifickým rozsahem oprávnění a odlišným uživatelským rozhraním.

2.1.1 Neregistrovaný návštěvník (Veřejnost)

Tato role reprezentuje především rodiče a obyvatele Havlíčkova Brodu hledající aktivitu. Hlavní prioritou je zde rychlost přístupu k informacím bez nutnosti autentizace. Mezi klíčové funkcionality patří:

- Prohlížení a filtrace:
Možnost okamžitého
třídění kroužků podle kategorií (sport, hudba,
technika, jazyky), věkuúčastníka,lokalityvrámci
města a časové dostupnosti.
- Detail kroužku: Zobrazení komplexních informací včetně popisu aktivity, ceny, kapacity a kontaktů na odpovědné osoby.
- Profily trenérů:
Přístup k informacím o
odbornosti trenérů a jejich kompletní nabídce
aktivit.

2.1.2 Trenér / Organizátor

Role určená pro poskytovatele služeb. Vyžaduje registraci a následné přihlášení. Tato role transformuje systém z pasivního katalogu na aktivní platformu pro správu obsahu.

- Správa profilu:
Možnost prezentovat své
zkušenosti a odbornost veřejnosti.
- Publikační činnost: Rozhraní pro přidávání
nových kroužků pomocí strukturovaného formuláře, který minimalizuje riziko chybějících
údajů.
- Aktualizace dat: Možnost v reálném čase měnit
stavy kroužků (např. označení kroužku jako „obsazený“), což zabraňuje dezinformaci zájemců.

2.1.3 Administrátor

Role dohlížející na integritu a kvalitu obsahu. Administrátor plní funkci moderátora, který zajišťuje, aby systém nebyl zneužit k šíření nevhodného obsahu nebo duplicitních záznamů.

- Schvalovací proces: Kontrola nově přidaných
kroužků před jejich zveřejněním pro veřejnost.
- Správa kategorií: Úprava struktury systému dle
aktuální poptávky ve městě.
- Moderace uživatelů: Správa trenérských účtů a
řešení technických dotazů.
- Moderace uživatelů: Převod kroužků na stránce
na reálného majitele.

### 2.2 User Stories (Uživatelské scénáře)

Pro lepší pochopení interakce uživatelů se systémem byly definovány typické scénáře, které reflektují reálné potřeby obyvatel Havlíčkova Brodu:

### 1. Scénář Rodič: „Jako matka školáka hledám pro svého syna kurz angličtiny v docházkové

vzdálenosti od centra města. Potřebuji vidět nejen cenu a čas, ale i profil lektora, abych měla jistotu o kvalitě výuky. Díky filtru na webu najdu relevantní nabídky během několika sekund a rovnou kontaktuji vybraného trenéra.“ 2. Scénář Trenér: „Jako zakladatel nového oddílu karate v HB potřebuji oslovit co nejvíce rodičů. Vytvořím si profil na portálu Kroužky Vysočina, nahrajiinformaceonáboruaposchváleníadministrátorem se moje nabídka zobrazí všem zájemcům v kategorii sport. Nemusím tak investovat do vlastního webu a SEO.“ 3. Scénář Administrátor: „Zaregistroval se nový uživatel jako trenér tenisu. Zkontroluji jeho profil, ověřím, zda jsou údaje o kroužku kompletní a srozumitelné, a jedním kliknutím kroužek publikuji. Systém tak zůstává přehledný a profesionální.“

### 3. Návrh řešení a architektura

V této kapitole je popsán technický rámec aplikace, zvolené technologie a vnitřní logika správy dat. Architektura byla navržena s důrazem na rychlost odezvy, bezpečnost dat a snadnou škálovatelnost.

### 3.1 Technologický stack

Pro vývoj portálu Kroužky Vysočina byla zvolena moderní kombinace technologií, které umožňují rychlé nasazení a efektivní správu.

- Frontend: Next.js (React Framework): Volba
Next.js byla podmíněna požadavkem na vysoký
výkon a optimalizaci pro vyhledávače (SEO). Díky
technologii Server-Side Rendering (SSR) jsou
profily kroužků indexovatelné vyhledávači, což
zvyšuje šanci, že rodiče najdou aktivitu přímo
přes Google či Seznam.
- Backend a Databáze: Firebase (BaaS): Platforma Firebase od společnosti Google byla
využita jako komplexní backendové řešení.

– Firestore: Dokumentová NoSQL databáze umožňující real-time synchronizaci dat mezi trenérem a návštěvníkem. – Firebase Authentication: Zajišťuje bezpečné přihlašování trenérů pomocí e-mailu či Google účtu. – Cloud Storage: Slouží pro ukládání fotografií kroužků a profilových obrázků trenérů. • Styling: Tailwind CSS: Pro zajištění plné responzivity napříč mobilními zařízeními a desktopy byl použit utility-first framework Tailwind CSS.

### 3.2 Datový model a životní cyklus kroužku Klíčovým prvkem systému je stavový automat, který řídí viditelnost kroužku na webu. Každý kroužek v databázi obsahuje atribut status, který nabývá jedné ze čtyř hodnot:

### 1. Draft (Rozepsáno): Kroužek je uložen v soukromé sekci trenéra. Není viditelný pro veřejnost ani pro administrátora. Slouží k postupnému vyplňování dat. 2. Pending (Čeká na schválení): Po odeslání trenérem se kroužek uzamkne pro úpravy a zobrazí se v administrativním rozhraní ke kontrole. 3. Published (Publikováno): Po schválení administrátorem je kroužek veřejně dohledatelný v katalogu. 4. Archived (Archivováno): Po skončení sezóny nebo naplnění kapacity může být kroužek stažen z nabídky, ale data zůstávají v databázi pro budoucí potřeby (např. exporty pro příští rok).

### 3.3 Workflow systému: Od formuláře k publikaci

Proces zveřejnění aktivity byl navržen tak, aby byla zajištěna maximální kvalita dat:

### 1. Vstup dat: Trenér v přihlášené zóně vyplní formulář (název, kategorie, věkové rozmezí, cena, čas a místo konání v Havlíčkově Brodě). 2. Validace: Systém na straně klienta i serveru ověří integritu dat (např. zda není cena záporná nebo zda nechybí kontakt). 3. Notifikace administrátora: Po odeslání do stavu Pending je administrátor upozorněn na nový požadavek ke schválení. 4. Moderace: Administrátor zkontroluje věcnou správnost. Má možnost kroužek schválit, nebo vrátit k dopracování s komentářem. 5. Distribuce: V okamžiku schválení Firestore okamžitě aktualizuje veřejný seznam kroužků bez nutnosti obnovy stránky u koncových uživatelů.

### 4. Infrastruktura a zabezpečení dat

Vzhledem k tomu, že aplikace pracuje s osobními údaji trenérů a uživatelů, byl při návrhu kladen extrémní důraz na bezpečnostní architekturu. Využití platformy Firebase jako „Backend-as-a-Service“ (BaaS) umožniloimplementovatstandardyzabezpečení, které jsou běžné u komerčních aplikací.

### 4.1 Autentizace a správa uživatelských relací

Správa identit je realizována pomocí služby Firebase Authentication. Systém nevyužívá lokální ukládání hesel v prostém textu, ale deleguje tuto odpovědnost na infrastrukturu společnosti Google.

- OAuth 2.0:
Implementace přihlášení přes
Google účet zvyšuje uživatelský komfort a
bezpečnost.
- Token-based Security: Po úspěšném přihlášení
je uživateli vygenerován unikátní token (JWT),
který autorizuje každý požadavek směrem k
databázi.

### 4.2 Firestore Security Rules (Databázová vrstva)

Klíčovým prvkem ochrany dat v tomto projektu jsou tzv. Security Rules. Na rozdíl od klasických SQL databází, kde ochranu řeší serverová logika, zde pravidla běží přímo na straně databázového stroje.

- Ochrana soukromí: Pravidla jsou nastavena tak,
že dokument v kolekci users může číst a měnit
pouze autentizovaný vlastník daného UID.
- Integrita kroužků: Editace dokumentu v kolekci
clubs je povolena pouze v případě, že UID přihlášeného uživatele odpovídá poli trainerId u
daného záznamu.
- Validace na úrovni schématu: Pravidla striktně
kontrolují datové typy příchozích polí, čímž se
předchází pokusům o injekci nevalidního kódu
nebo poškození datové struktury.

### 4.3 Cloud Hosting a CI/CD proces

Aplikace je hostována na platformě Vercel, která je nativně optimalizována pro framework Next.js. Pro zefektivnění vývoje byl nastaven proces Continuous Integration / Continuous Deployment (CI/CD).

### 1. Verzování kódu: Veškeré změny jsou spravovány v repozitáři systému GitHub. 2. Automatizovaný Build: Při každém „pushi“ do hlavní větve (main) Vercel automaticky spustí proces sestavení aplikace, provede kontrolu syntaktických chyb a v případě úspěchu aplikaci nasadí do produkčního prostředí. 3. SSL Certifikace: Veškerý provoz mezi koncovým zařízením a serverem je šifrován pomocí automaticky obnovovaných SSL certifikátů, což garantuje ochranu dat při přenosu (HTTPS).

### 5. Uživatelské rozhraní (UI) a UX Design

Kvalita uživatelského rozhraní přímo ovlivňuje úspěšnost platformy v lokální komunitě. Návrh

byl veden snahou o maximální přehlednost, aby i technicky méně zdatní uživatelé dokázali snadno najít relevantní informace.

### 5.1 Vizuální identita

Vizuální styl portálu vychází z loga projektu „Kroužky Vysočina“, které kombinuje moderní typografii s přívětivou barevnou paletou.

- Barevné schéma: Dominantním prvkem je
tyrkysová barva (#2ab7a9), která evokuje energii
a aktivitu. Tato barva je využita pro klíčové akční
prvky (CTA tlačítka), jako je „Zobrazit kroužky“
nebo „Vytvořit“. Doplňkovou barvou je tmavě námořnická modř, použitá pro nadpisy a navigaci,
zajišťující vysoký kontrast a čitelnost.
- Typografie: Pro celý portál byl zvolen čistý bezpatkový font (Sans-serif), který působí moderně
a je dobře čitelný na digitálních obrazovkách
různých rozlišení.

### 5.2 Responzivita a mobilní zobrazení

Vzhledem k analýze, která ukázala, že více než 60 % rodičů přistupuje k informacím z mobilních telefonů, byl kladen extrémní důraz na responzivní design.

- Adaptivní layout: Pomocí Tailwind CSS byl implementován systém mřížky (grid), který se automaticky přeskládá z dvousloupcového či třísloupcového zobrazení na PC do jednoho sloupce
na mobilu.
- Dotykové ovládání: Tlačítka a ovládací prvky filtrace byly zvětšeny tak, aby splňovaly standardy
pro snadné ovládání prsty (minimálně 44x44 px).
- Navigační menu: Na mobilních zařízeních se
horní lišta transformuje do tzv. „hamburger
menu“, čímž se šetří drahocenný prostor na obrazovce.

### 5.3 Wireframes vs. Realita

Proces návrhu začal tvorbou drátěných modelů (wireframes), které definovaly rozložení prvků bez vlivu barev. Hlavní rozdíl mezi návrhem a realizací spočíval v jemném doladění rozestupů...

Hlavní rozdíl mezi návrhem a realizací spočíval v jemném doladění rozestupů (whitespace). Finální verze využívá vzdušnější layout, který pomáhá uživateli soustředit se na vyhledávací pole jako na primární interakční bod.

V Havlíčkově Brodě

Všechny volnočasové aktivity pro děti i dospělé na jednom místě.

Sport, hudba, jazyky, technika a mnoho dalšího.

Zobrazit kroužky

50+ kroužků Havlíčkův Brod 30+ trenérů

Proč kroužky HB?

Vše, co potřebujete vědět o volnočasových aktivitách ve městě, najdete na jednom

místě.

Snadné vyhledávání

Filtrujte kroužky podle věku, kategorie, lokality nebo času. Najděte přesně to, co hledáte.

Prověření trenéři

Všichni trenéři mají ověřené zkušenosti a certifikace. Můžete jim důvěřovat.

Aktuální informace

Ceny, časy, volná místa - vše aktualizované přímo trenéry. Žádné překvapení.

Prozkoumejte kategorie

Od sportu po umění - najdete u nás širokou škálu aktivit

Sport Hudba Jazyky Technika

Umění Tanec Věda Ostatní

Kroužky Vysočina

powered by WAFK

Centrální katalog volnočasových kroužků a trenérů v Havlíčkově Brodě pro děti i dospělé. Sport, hudba, jazyky, technika a mnoho dalšího.

Rychlé odkazy

Kroužky

Trenéři

Kategorie

O nás

Kontakt

Havlíčkův Brod, Vysočina

krouzky.vysocina@gmail.com

+420 606 041 893

© 2026 Kroužky Vysočina. Všechna práva vyhrazena.

Najděte ten pravý kroužek

pro vás

Hledat

Kroužky Vysočina

powered by WAFK

Kroužky Trenéři Josef Holeček Moje Vytvořit Odhlásit Administrace

20.03.2026, 12:08

Page 1 of 1

Obrázek 1. Srovnání wireframu a finální implementace.

### 6. Vize a budoucí rozvoj systému

Ačkoliv je portál v současné verzi plně funkční a připraven k nasazení, jeho modulární architektura přímo vybízí k dalšímu rozšiřování, které by z něj vytvořilo komplexní komunitní platformu pro celou Vysočinu.

### 6.1 Plánované funkční rozšíření

V horizontu příštího vývoje jsou uvažovány následující moduly:

### 1. Integrovaný rezervační a přihlašovací systém: Aktuálně web slouží jako informační katalog. Dalším krokem je implementace modulu pro přímé online přihlašování, včetně správy kapacit v reálném čase a generování přihlášek ve formátu PDF. 2. Platební brána: Propojení s platebním systémem (např. Stripe nebo GoPay) by umožnilo rodičům okamžitou úhradu členských příspěvků či zápisného přímo přes portál, což by výrazně snížilo administrativní zátěž trenérů. 3. Geolokační služby a interaktivní mapa: Integrace Mapy.cz API pro vizualizaci všech kroužků na mapě Havlíčkova Brodu. Uživatelé by tak mohli vyhledávat aktivity nejen podle věku, ale

i podle docházkové vzdálenosti od bydliště či školy. 4. Personalizovaný kalendář akcí: Systém, který by registrovaným uživatelům zasílal notifikace o blížících se náborech, dnech otevřených dveří nebo jednorázových turnajích na základě jejich preferencí. 5. Mobilní aplikace (PWA): Převod webu do formy Progressive Web App, což by umožnilo instalaci portálu přímo na plochu telefonu a využití push notifikací pro okamžitou komunikaci mezi trenérem a rodičem.

Projekt „Kroužky Vysočina“ má ambici stát se standardem pro digitální prezentaci volnočasových aktivit v regionu. Věřím, že jeho nasazení do reálného provozu by výrazně přispělo k digitalizaci místní samosprávy a ke zvýšení zapojení dětí a mládeže do organizovaných aktivit.

### 7. Závěr a zhodnocení přínosu projektu

Předkládaný maturitní projekt „Portál Kroužky Vysočina“ vznikl jako reakce na reálnou potřebu centralizace informací o volnočasových aktivitách v regionu Havlíčkův Brod. Cílem práce bylo vytvořit robustní, bezpečné a uživatelsky přívětivé webové

rozhraní, které by eliminovalo informační šum a usnadnilo komunikaci mezi organizátory (trenéry) a koncovými uživateli (rodiči a zájemci o seberozvoj).

### 7.1 Dosažené cíle a technické zhodnocení

V rámci vývoje se podařilo úspěšně implementovat moderní full-stack architekturu postavenou na frameworku Next.js 15 a platformě Firebase. Zvolené technologie se ukázaly jako vysoce efektivní pro typ aplikace, která vyžaduje real-time synchronizaci dat a vysokou úroveň zabezpečení bez nutnosti správy vlastního serveru.

Hlavní technické milníky, které byly v rámci projektu splněny:

- Centralizace dat: Vytvoření jednotného schématu pro různé typy aktivit (sport, hudba, technika).
- Stavový automat:
Implementace schvalovacího workflow (Draft, Pending, Published),
který zajišťuje kontrolu kvality obsahu administrátorem.
- Typová bezpečnost: Využití TypeScriptu a schémat Zod pro eliminaci runtime chyb a validaci
vstupních dat.
- Responzivita: Návrh mobilního rozhraní pomocí Tailwind CSS, které odpovídá moderním
standardům UX/UI.

Z pohledu autora byla práce na tomto projektu nesmírněpřínosná. Přineslaminejenprohloubeníznalostí v oblasti frontendového vývoje, ale především mě naučila pracovat se serverless architekturou a logikou oprávněnínastranědatabáze(FirestoreSecurityRules). Projektmědonutiluvažovatowebujakookomplexním ekosystému, kde je nutné balancovat mezi potřebami běžného uživatele a nároky administrátora na správu obsahu.

### Poděkování

Na tomto místě bych rád upřímně poděkoval vedoucímu mé maturitní práce, panu Ing. Adamu Ferenczovi, za jeho odborné vedení, cenné rady a čas, který mi v průběhu vývoje tohoto projektu věnoval.

Dále mu děkuji za věcné připomínky k technickému řešení aplikace a za metodickou pomoc, která mi výrazně pomohla při zpracování této dokumentace. V neposlední řadě si vážím jeho trpělivosti a vstřícného přístupu, díky kterému bylo možné projekt úspěšně dokončit a nasadit do reálného provozu.