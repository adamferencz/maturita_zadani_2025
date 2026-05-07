# Podklady pro posudky — diktační formulář

**Jak to použít:** Pod každou otázku nadiktuj (nebo napiš) odpověď do bloku `> ...`. Délka libovolná, odrážky vítány. Až budeš hotový s některým studentem (nebo se všemi), řekni a já z toho vygeneruju posudek vedoucího i oponenta v jednotné struktuře a uložím je do `posudky/<student>/`.

**Legenda odpovědí:**
- `> ` — sem piš odpověď
- `> [Návrh: ...]` — předběžná analýza z odevzdaných materiálů (upřesni, potvrd nebo vyvrať)
- prázdno = ještě nevyplněno
- `[PŘESKOČIT]` = vynechat

---

## 1) Josef Holeček — *Webový portál pro kroužky a trenéry v Havlíčkově Brodě*

### Vedoucí (proces, student)

**V1.** Jak pravidelně a aktivně pracoval během roku? Držel se harmonogramu?
> Student pracoval průběžně a. Během roku docela aktivně. Err. Od samotného návrhu aplikace, přestože se musel veškeré technologie naučit od začátku po realizaci, dokonce se sám popasoval IS nasazením aplikace AS různými technickými problémy. V závěru bylo potřeba ho mírně motivovat k tomu, aby práci dotáhnul a dodělal tam určité věci. A např. a tam se dotáhl reálná data a hodnocení živých uživatelů jinak tady to bylo  

**V2.** Konzultoval, reagoval na zpětnou vazbu, nebo jsi musel něco vracet opakovaně?
> Student konzultoval, když bylo potřeba primárně v rámci hodin a zpětnou vazbou si bral k srdci. 

**V3.** Co musel řešit sám a v čem naopak potřeboval vést za ruku?
> V principu 95% věcí vyřešil sám a potřeboval jenom motivaci, případně nějaký teoretický úvod, který jsme dělali stejně v rámci výuky. 

**V4.** Testoval portál na reálných rodičích / trenérech / vedoucích kroužků? (zadání to u projektů s uživateli vyžaduje)
> Tady vidím nejslabší část vlastně celé práce. Jasně bylo zadání řečeno, že kromě vytvoření práce samotné, tak je potřeba jít dotáhnout i do reálného provozu. Aplikace je v provozu, ale není používána uživateli, což mohlo být dotaženo. Sice to není IT činnost, ale vlastně na základě té činnosti by vznikly další věci. Svoje řešit a takhle jsme nezjistili na reálných stanech to bylo otestováno. To znamená reálně trenéři vyplňovali své profily. Ale kroužky byly dělané pouze tím zakládáním za ty kroužky, což je ale dobrá fíčura, kterou tam přidal a reálně rodiče se k tomu nedostali, protože ta aplikace nebyla zveřejněná, což je za mě velké- a je to prostě škoda, že se to nedotáhlo.  

**V5.** Silné stránky studenta a kde má rezervy?
> Silnými stránkami studenta je. Učit se pracovat samostatně. Velmi se přizpůsobil práci SI nástroji. A dokonce si dokázal popasovat například i se situací, že bylo potřeba na firesteel zadat jako kreditní kartu. Sice to nic nestrhává alo nebo velmi málo, ale nelekl se toho a nezasekl se v rámci tady ty možnosti. Err. Takže vlastně samostatnost a. Nějaká nějaké přizpůsobení? AI design to a stránka má hezkej? AI schopnost prezentovat. V rámci hodin. Rezervy má v dotahování a samozřejmě v nějakých hlubších znalostech. Toho programovacího jazyka a nějakých technických oblastech. Jelikož. Ta práce byla hodně dělaná s pomocí IP, což není nutně špatně, ale v některých situacích. By to, kdyby se nám řekl něco, rozbilo, by tohle mohlo být limitující. 

### Oponent (výstupy)

**O1.** Jsou splněné funkční požadavky ze zadání? Co chybí nebo je jen formálně?
> [Návrh: Z dokumentace a kódu jsou prokazatelně splněny: veřejný katalog kroužků s filtrováním (věk, kategorie, lokace, typ) ✓, profily trenérů se správou vlastních kroužků ✓, admin panel pro schvalování/zamítání příspěvků ✓, real-time data přes Firestore ✓, responzivní design ✓. Slabé místo: Firestore security rules jsou v dokumentaci označeny jako "dočasně otevřené pro vývoj" (`allow create, update, delete: if true`) — pokud takto jede i produkce, je to bezpečnostní díra. README je prázdný placeholder ("Dopln..."), takže onboarding pro cizího vývojáře začíná rovnou technickou dokumentací.]
Jo aplikace splňuje vše, co je potřeba. 

**O2.** Článek (4–15 stran) — kvalita textu, struktura, reference.
> [Návrh: PDF článek existuje a byl odevzdán. Obsah PDF nemohu přečíst přímo — toto musíš vyhodnotit ty. Zadání vyžadovalo: analýzu potřeb komunity, návrh UI, implementaci, testování použitelnosti.]
Jo, hele za mě článek splňuje všechno jakkoli toho textu strukturou, tak i tímto se v něm píše. Takže za mě článek je v pořádku. 

**O3.** Technická dokumentace (MD) — stačila by cizímu vývojáři k zprovoznění portálu?
> [Návrh: Dokumentace má 1 032 řádků (verze 1.0, březen 2026) a je velmi komplexní. Pokrývá: přehled systému, tech stack tabulku, strukturu repozitáře, instalaci, Firestore schéma (5 kolekcí), stavové workflow, auth/authz, routing (16 veřejných + 7 chráněných tras), 5 vlastních hooků, nahrávání souborů, security rules, deployment na Vercel, troubleshooting. Cizí vývojář by podle ní nasazení zvládl — ale narazí na problém s otevřenými security rules, pokud je neupraví.]
Jo hele tohle to je v pohodě+ na ty security rules tak tam. Můžem dát nějakej dotaz? Zeptat se, jak to funguje na obhajobě?


**O4.** Poster — čitelnost na A3 a obsahové poselství.
> [Návrh: PDF poster existuje. Grafickou a obsahovou kvalitu nemohu vyhodnotit — toto musíš posoudit ty.]
UU stroje graficky hezkej Přehledné a dá se podle toho pochopit smysl práce. 

**O5.** Je portál reálně nasazený a používaný, nebo "jen funguje lokálně"?
> [Návrh: Portál je nasazený na Vercel + Firebase (ne jen lokálně). Trenéři reálně vyplňovali profily dle tvého V4. Reálná rodičovská aktivita prokazatelně chybí — aplikace nebyla veřejně publikována. Security rules jsou potenciálně stále vývojové (otevřené). Technická infrastruktura pro ostrý provoz je připravená, ale spuštění do plného provozu neproběhlo.]
Tak co se týče nasazení, tak tady. Je největší slabina Err. Aplikace by uživatelské testováním Um. Prošla ale prošla pouze lokálním testováním, nebyla testována na reálných komerčních uživatelích a tedy. Není prokázané, že je uživatelsky přívětivá a že by byla používána. A to je asi jediný co vytknout

---

## 2) Jakub Jakůbek — *Webová aplikace pro distribuci školních propagačních předmětů (GHB Merch)*

### Vedoucí

**V1.** Průběh a pravidelnost práce, reakce na zpětnou vazbu?
> [Toto musíš vyhodnotit ty — vychází z osobních zkušeností z hodin a konzultací.]
Student pracoval samostatně. V některých fázích err bylo potřeba ho popostrčit, aby err dodělal určité komplexnější věci, které by jinak dělat nechtěl. A tím, že jsem byl pod postrkovat, tak ta práce. Se jako dotáhla dobře.  

**V2.** Sám si sháněl requirementy (škola, velikosti, sklad, platby) nebo jsi mu je musel formulovat?
> [Toto musíš vyhodnotit ty. Poznámka z technické stránky: scope projektu je velmi konkrétní a reálný (batch objednávky s minimálním množstvím, QR výdej, Microsoft SSO pro @ghb.cz účty) — to nasvědčuje, že student aktivně zmapoval reálné potřeby školy.]
Sám chodil na schůzky s. Vlastně potenciálním klientem, který bude dělat administrátora tomu systému pro školní merch. A. Na základě tady těch schůzek. Err. Dělal aktualizace samostatně. Přesně jak píšeš, tak jako velmi dobře vymyslel různý fakt, způsoby, který by ani toho zadavatele nenapadly, že se takhle dá řešit. 

**V3.** Největší technická / organizační překážka a jak ji vyřešil?
> [Toto musíš vyhodnotit ty z vlastní zkušenosti. Z dokumentace je vidět několik netriviálních problémů, které musel vyřešit: Svelte 5 s Runes API (relativně nové, vydáno říjen 2024 — student šel do cutting-edge frameworku), vlastní Docker + Caddy deployment s automatickým HTTPS, HMAC validace QR kódů pro zabezpečený výdej, integrace Microsoft SSO pro školní účty.]
Za mě. Použil super technologie, položil nasazení do krize. Um QR kódy tam přidal integraci účtu Velmi komplexní uživatelský rozhraní. Err agentní vývoj, takže za mě super. 

**V4.** Byla aplikace ověřena se skutečnou objednávkou / reálnými uživateli ze školy?
> [Toto musíš vyhodnotit ty. Z technické stránky: aplikace je nasazená na vlastní doméně merch.jakubjakubek.cz s platným HTTPS (Let's Encrypt přes Caddy), má Docker Compose pro produkci. Infrastruktura pro reálný provoz je plně připravená.]
Tady je největší slabina. Nebyla tam tak velký tah na branku, aby sis sám zařídil včasné zprovoznění a aby reální uživatelé šli opravdu udělat reálnou objednávku. Proběhlo testování velkým množstvím uživatelů, vlastně celou třídou. Což cením, to je super. Err ale vyhrávky nebyly spuštěny, takže ještě možný, že tam třeba nějaký chyby budou, který budou až v realitě 

**V5.** Silné a slabé stránky studenta.
> [Toto musíš vyhodnotit ty z osobní zkušenosti. Technicky viditelné silné stránky: moderní fullstack (SvelteKit 5 + PostgreSQL 16 + Docker), vlastní produkční deployment, pokročilá bezpečnostní opatření (HMAC, httpOnly cookies, rate limiting). Slabé stránky z kódu nejsou zřejmé.]
Svejma stránkama studenta jsou zkušenosti a schopnost jako věci vymyslet a schopnost používat i já aj. Err. Slabé stránky je jsou občasné nedodržení termínů nebo některý věci nebyly brány dostatečně vážně. Err a. Tak i přes velké kvality studenta, tak třeba err ty výkony. Kde prostě Nebyly, nikdy si z toho dělal moc prdel. Já nevím, jak to mám vysvětlit. Někdy se z toho prostě děláš srandu.  

### Oponent

**O1.** Splnění funkčních požadavků — objednávkový portál, role, sklad, export, …?
> [Návrh: Z dokumentace jsou prokazatelně splněny: katalog produktů s barevnými/velikostními variantami ✓, batch objednávkový systém s minimálními množstvími ✓, 3 role (user / admin / superadmin) ✓, QR kódy pro výdej s HMAC ověřením ✓, admin panel s lifecycle sledováním objednávek ✓, statistiky a reporting dashboard ✓, Microsoft SSO pro @ghb.cz ✓. 5 stavů objednávky (pending_batch → processing → ready → completed / cancelled) ✓. API health endpoint ✓.]
Jo přesně tak, jak si to prošel, tak. Ano. Všechno, co je potřeba, tak splnil. 

**O2.** Kvalita článku (PDF `Maturitní_projekt___GHB___2026`) — struktura, argumentace.
> [Návrh: PDF článek existuje. Obsah PDF nemohu přečíst — toto musíš vyhodnotit ty. Zadání vyžadovalo: analýzu objednávkového procesu, UX design, implementaci, testování použitelnosti.]
Ano článek je dostatečně kvalitní a dobře strukturovaný, dobře dlouhý, takže a píše se v něm vše podstatné. A co mi ve článku chybí, tak je možná lepší popis třeba administrátorského rozhraní. Který byl dost kvalitní AV článku, to není dostatečně třeba na screenshotu ovaný a víc popsaný.  

**O3.** Dokumentace (MD) — instalace, deploy, datový model, API. Je kompletní?
> [Návrh: Dokumentace má 800 řádků (březen 2026) a je jedna z nejpropracovanějších. Pokrývá: kompletní DB schéma (8 hlavních tabulek s detailními popisy a constrainty), 14+ API endpointů s request/response příklady, routing (24 veřejných + 13 admin stránek), email systém (6 typů emailů), zpracování obrázků (AVIF, max 1200px), security opatření, kompletní deployment guide s Dockerem. Instalace podle dokumentace by měla být reprodukovatelná.]
Tím, jaké aplikace komplexní, tak i dokumentace komplexní, což je správně. Um takže super.  

**O4.** Bezpečnost — GDPR, hesla, soubory, autorizace.
> [Návrh: HMAC validace QR kódů ✓, httpOnly cookies ✓, rate limiting ✓, soubory mimo webroot ✓ (upload security popsán), hesla přes Better Auth 1.3+ ✓, HTTPS přes Let's Encrypt ✓. GDPR — v dokumentaci explicitně nezmiňováno, toto musíš vyhodnotit ty (co se sbírá o uživatelích, jak dlouho se uchovává). SQL injection — Drizzle ORM chrání parametrizovanými dotazy ✓.]
Err řešit GDPR nebylo součástí zadání, takže to bych vůbec neřešil. A jinak to, co píšeš, tak je ideální. 

**O5.** Poster (GHB Merch) — vizuálně a obsahově.
> [Návrh: PDF poster existuje. Grafiku a obsah nemohu vyhodnotit — toto musíš posoudit ty.]
Napster byl užita II. Přehledný a dobrý. Čekal bych v něm akorát větší množství screenshotů. 

**O6.** Je řešení reálně použitelné pro výdej na škole, nebo je to demo?
> [Návrh: Technicky je to produkčně připravené řešení — vlastní doména s HTTPS, Docker Compose, automatické logy, doporučené UptimeRobot monitorování. Jestli proběhla reálná objednávka nebo výdej na škole, to musíš potvrdit ty.]
Řešení bude reálně využité na škole. Err v době, kdy píšu tady to hodnocení, tak se. Pořídil hosting a měl by jakubek pracovat na nasazení na dálný hosting. Měl to už 1. Nasazený na svém vlastním hostingu, který ale zrušil z důvodu toho, že nemá smysl ho platit a škola mu teďka pořídila teda hosting a. Pravděpodobně ještě před maturitami dokončí nasazení. 
---

## 3) Mark Joly — *VTOL letoun schopný přenášet komunikační modul*

### Vedoucí

**V1.** Průběh — stavba, testování, opravy po haváriích?
> [Toto musíš vyhodnotit ty — průběh stavby a havárie vidíš jen ty z osobní zkušenosti. Z odevzdaných materiálů: existují fotografie z výroby (Fotografie/), ArduPilot export konfigurace, 3D rendery a výkresy, videa letů na Google Drive. To naznačuje, že letoun skutečně létal.]
Ano letoun skutečně létal, bylo to úspěšné. Err rozhodně lépe než jejich předchozí letoun z minulého roku a Dal bych tomu létání 8 a půl bodu z 10, což je velmi jako dobrý. Kde 10 bodů z 10 by bylo, že to lítá jako totální raketa Obecně opět velmi těžké zadání, které bylo velmi dobře zvládnuto. A velmi nad rámec 

**V2.** Spolupráce s Mikuličem (komunikační modul jako náklad).
> [Toto musíš vyhodnotit ty. Z technické stránky: Mikuličův modul je navržen pro 2S LiPo napájení (5–8,4 V) a byl testován na letounu. Mikuličova dokumentace zmiňuje "reálné testování" dosahu — to předpokládá spolupráci s Jolym. Konkrétní koordinaci rozhraní, hmotnosti a napájení musíš potvrdit ty.]
Ano letoun létal reálně s reálným modulem a přes ten rozšiřovací kanál to vždycky komunikoval, takže to je v pohodě. 


**V3.** Kolik iterací / verzí prošel? Co se ne/povedlo?
> [Toto musíš vyhodnotit ty — počet iterací a havárie vidíš jen ty. Z repozitáře je znát, že výroba proběhla (fotodokumentace, CAD soubory, výkresy, ArduPilot konfigurace exportována).]
Iterací podle mě bylo docela dost, ale méně než v předchozím roku, kdy dělali ještě jinej typ letounu, takže tam už měli nějaké zkušenosti. Každopádně tenhle tenhleten je opravdu o level výš i designem a tímhle. 


**V4.** Létá letoun stabilně a zvládne ≥ 250 g? Viděl jsi let na vlastní oči?
> [Toto musíš vyhodnotit ty — záleží na tom, co viděl jsi osobně. Z dostupného: videa letů jsou na Google Drive (odkaz odevzdán). Minimální nosnost 250 g byl požadavek zadání — splnění je nutné ověřit z videí nebo osobně.]
Led je zaznamenán na video.Opravdu zvládne, zvládne nést ten náklad a. Tedy to splnili 


**V5.** Silné a slabé stránky studenta (hardware vyžaduje jinou sadu dovedností).
> [Toto musíš vyhodnotit ty z osobní zkušenosti. Technicky viditelné: student zvládl CAD modelování, výrobu z carbonu/EPP/3D tisku, konfiguraci ArduPilot autopilota — to je netriviální kombinace dovedností pro gymnazistu.]
Student zpracovával pečlivě jak svůj projekt, tak potom i následnou dokumentaci. Projekt byl velmi netriviální, ale byl super práci. 


### Oponent

**O1.** Splnění zadání — VTOL režim, horizontální let, nosnost 250 g, přenos modulu. Co je prokazatelně splněno, co jen deklarováno?
> [Návrh: Prokazatelně odevzdáno: ArduPilot export konfigurace ✓, fotodokumentace z výroby ✓, 3D rendery a technické výkresy ✓, videa letů ✓ (Google Drive). VTOL schopnost a horizontální let — ověřitelné z videí, toto musíš posoudit ty. Nosnost 250 g a integrace s komunikačním modulem — vyžaduje potvrzení z videí nebo osobního pozorování. README je minimální (11 řádků), žádné detailní textové shrnutí výsledků.]
Tak jak píšeš všechno jako nevzdal to, že rybník je velmi krátké, tak je možný. Tam můžeš takhle zmínit, ale to je úplně irelevantní. Ne? To tam ani jako nezmiňuj, to je prostě prostě reálný. Tam mělo bejt jenom jako velmi krátce, navíc animální programátorské. Projekt takže to je 1 


**O2.** Článek a metodika testování letových vlastností (dolet, stabilita, nosnost).
> [Návrh: PDF článek existuje. Zadání vyžadovalo: aerodynamická analýza, elektronický design, CAD design, výrobní proces, letové testy + kalibrace (8–15 stran). Obsah PDF nemohu přečíst — toto musíš vyhodnotit ty. Klíčová otázka: jsou v článku konkrétní naměřená čísla (dolet, výdrž baterie, maximální nosnost), nebo jen popis procesu?]
Metodika testování je super, splnili vše, co slíbili a možná ještě více zároveň. Co se týče článků, tak článek je velmi kvalitní, stejně jako všechny ostatní, teda nemateriální a. Err zároveň student err, byl autorem šablony článku.  

**O3.** Technická dokumentace (PDF) — stačí cizímu člověku na reprodukci (BOM, schémata, postup stavby, nastavení FC)?
> [Návrh: PDF technická dokumentace existuje. Obsah PDF nemohu přečíst přímo. Odevzdané podklady zahrnují: ArduPilot konfigurace (exportované parametry) ✓, technické výkresy (Vykresy/) ✓, 3D rendery (Renders/) ✓, fotodokumentaci (Fotografie/) ✓. Jestli jsou v dokumentaci kompletní BOM (seznam součástek s PN), drátová schémata a postup kalibrace FC, musíš posoudit ty z PDF.]
 Technická dokumentace je velmi kvalitní práce, samo o sobě je to PDF, které bylo originálně psané v latexu a. Err. Takže je velmi kvalitní. 

**O4.** Poster — graficky a obsahově.
> [Návrh: PDF poster existuje. Zadání vyžadovalo 3D vizualizace, fotografie letounu a charakteristiky. Grafiku a obsah nemohu vyhodnotit — toto musíš posoudit ty.]
Plakát je vizuálně velmi hezký a obsahuje 3 d vizualizace a fotografie letounu, takže to je super. 

**O5.** Neodevzdal prezentaci — jak to vnímáš? (zadání to umožňuje, ale je to signál)
> [Návrh: Prezentaci odevzdal — ale pozdě. PR byl mergován 7. 5. 2026 (dnes). Odevzdal: PDF prezentaci bez videa + Canva odkaz s prezentací s videi letů. Tedy materiál existuje, jen nebyl v repozitáři od začátku. Zda to stačí z hlediska termínu, musíš posoudit ty.]
Student odevzdal prezentaci včas jenom já jsem tu martial pozdě, to znamená všechno je v pořádku. Prezentace je velmi kvalitní, prezentovaná včas a obsahuje i videa, to znamená tady je vše splněno. 


**O6.** Bezpečnost provozu a legislativa (registrace, pravidla ÚCL).
> [Návrh: Toto nemohu vyhodnotit z dostupných materiálů — v README ani dokumentaci zmínka o registraci dronu u ÚCL nebo splnění nařízení EU 2019/945 není. Toto musíš vyhodnotit ty — jde o důležitou otázku u hardwarového projektu s letounem.]
Student testoval na bezpečném místě na veřejném nebo jako na prostranství, kde nemohl nikoho ohrozit v dohledové vzdálenosti, to znamená, neporušil žádnou legislativu a všechno dodržel, takže to bylo taky správně uděláno. 

---

## 4) Jiří Kotlas — *Project Manager — systém na řízení firemních procesů a dokumentů*

### Vedoucí

**V1.** Průběh práce — pravidelnost, tempo, držení harmonogramu?
> [Toto musíš vyhodnotit ty z osobní zkušenosti.]
Student se učil v framework kách zcela od začátku, a proto udělal velký kus práce udělal docela těžké zadání a. Pracoval adekv. Ať rychle dobrém tempu a harmonogram držel. 


**V2.** Rozsah je nadprůměrný (22 entit, ACL s Votery, Symfony 7.4, Docker). Nafoukl scope, nebo odpovídá reálné potřebě? Zvládl ho dotáhnout?
> [Návrh: Rozsah je objektivně velký — 22 Doctrine entit, 14 controllerů, 13 form typů, 60 Twig šablon, 16 migrací, 35+ tras, 9 stavových workflow. Kompletní business flow: klienti → projekty → nabídky → objednávky → smlouvy → akceptační protokoly → faktury. To je enterprise architektura. Zda odpovídá reálné potřebě nebo jde o nafouknutý scope, musíš posoudit ty. Z dokumentace ale vyplývá, že jednotlivé moduly jsou do sebe provázané a systém jako celek dává smysl.]
Ano, přesně tak, je to komerční projekt, který má aspiraci na nasazení v reálném v reálné firmě. A. Velmi samostatně všechno splnilo. Takže zároveň i konzultoval s reálným klientem a to vše. To vše je. Super výkon.  

**V3.** Samostatnost — architektonická rozhodnutí sám, nebo s výraznou pomocí?
> [Toto musíš vyhodnotit ty. Technicky: volba Symfony 7.4 + Doctrine Voters pro ACL + Docker je zralá a dobře odůvodněná architektura, která nevypadá jako náhodná AI halucinace — spíš jako někdo, kdo rozumí návrhům.]
Student nepotřeboval výraznou pomoc a konzultoval adekvátně vycházel ze zadání, které odpovídalo firmě. Teda to po požadovala A tady v tom dobře zvládnul.  

**V4.** Reální testeři (firma, rodič, někdo z praxe) nebo jen self-review?
> [Toto musíš vyhodnotit ty. Z kódu/dokumentace: existuje fixture loader s 19 testovacími uživateli, 17 klienty, 38 projekty, 47 nabídkami, 11 objednávkami, 10 smlouvami, 50 fakturami — to je solidní testovací sada. PHPUnit testy existují (dokumentace je označuje jako "průběžně rozšiřované"). Reální firemní uživatelé — musíš potvrdit ty.]

To student měl testery jednak self testing. Potom měl testy z řad spolužáků, kteří hráli roli testeru a byli velmi důslední. Err. Měl tam dobrou testovací sadu a zároveň to testovali potom i reální klienti, kteří teoreticky v budoucnu mohou práci převzít.


**V5.** Silné a slabé stránky studenta.
> [Toto musíš vyhodnotit ty z osobní zkušenosti. Technicky viditelné silné stránky: produkčně připravená infrastruktura (Docker, VPS deployment guide), sofistikovaná ACL s Voter pattern, výjimečně podrobná dokumentace (nejkompletnější ze všech 5 projektů — 1 111 řádků).]

Student prokázal silnou stránku tím, že se dál že cílevědomý ambiciózní. Dokáže se do něčeho postavili pracovat a zároveň se naučit novou věc. Err slabý stránky bych teda ani nezmiňoval. Je to v pohodě. Uděláme radost.  

### Oponent

**O1.** Splnění funkčních požadavků — CRUD všech modulů + ACL + reporty. Všechno funkční end-to-end?
> [Návrh: Z dokumentace jsou prokazatelně splněny: CRUD pro všechny moduly (klienti, projekty, nabídky, objednávky, smlouvy, protokoly, faktury) ✓, ACL s 3 Voter třídami ✓, dashboard s KPI ✓, reporty s grafy (Chart.js) ✓, stavová workflow pro 9 typů dokumentů ✓, email notifikace ✓, file upload mimo webroot ✓, reset hesel ✓. Zda jsou všechny moduly funkční end-to-end (bez skrytých chyb), musíš ověřit ty při testování aplikace.]
Tak funkčnost modulů za mě je to dostatečně prověřený testování a prezentoval to živě tak, že je to ok. 

**O2.** Článek — úroveň odborného textu, nebo převyprávěný README?
> [Návrh: PDF článek existuje. Obsah nemohu přečíst — toto musíš vyhodnotit ty. Klíčová otázka: je tam analýza problému a zdůvodnění architektonických rozhodnutí, nebo jen popis co systém dělá?]
Clanek je super, je tam napsaný, všechno velmi podrobně oceňuji. JA generovaný různý přehledy a diagramy. Ty jsou velmi přínosný, mohly bejt a ono to v těch 2 sloupcových formátech je možný. Je to povolený klidně na full, to znamená zabrat oba sloupce a tím bejt víc vidět. Malinko by se to celý protáhlo a zároveň tam v tom Spánku co teda bych vytknul tak chybí úvodní obrázek, což je povinná součást všech článků, takže bys uviděl obrázku není zas tak hezký. 

**O3.** Dokumentace (MD) — deployment, datový model, ACL model. Úplná a reprodukovatelná?
> [Návrh: Dokumentace je nejkompletnější ze všech 5 projektů — 1 111 řádků. Pokrývá: kompletní deployment (DEPLOYMENT.md na VPS), datový model všech 22 entit se schématy a vztahy, ACL model s popisem Voter tříd a rolí, 35+ tras, fixture data, 10 troubleshooting scénářů. Reprodukovatelná by měla být — Docker Compose + migrations by měly stačit.]
Tak technická technická dokumentace je dostačující. A prostě vzpomínáš.  

**O4.** Pokrytí testy — student sám píše "průběžně rozšiřováno". Kolik reálně?
> [Návrh: PHPUnit testy existují, ale konkrétní pokrytí (%) není v dokumentaci uvedeno. Formulace "průběžně rozšiřováno" naznačuje, že pokrytí není kompletní. Konkrétní počet testů a co pokrývají musíš ověřit ty (např. `php bin/phpunit --coverage-text`).]
Můžeš si ho klidně na ty unit testy zeptat v rámci obhajoby až ledna? Otázky na obhajobu každopádně. Pokud píšeš že to testovalo, tak tam už není jako zásadní jaká procentuální.  

**O5.** Bezpečnost — upload mimo webroot, reset hesel, SQL injekce, CSRF. Stojí to na standardních Symfony primitivech správně?
> [Návrh: Upload mimo webroot ✓ (explicitně popsán v dokumentaci), reset hesel ✓ (vlastní flow dokumentován), SQL injection — Doctrine ORM s parametrizovanými dotazy ✓, CSRF — Symfony forms mají CSRF tokeny automaticky ✓, rolová hierarchie + Voters ✓, HTTPS doporučeno v deployment guide ✓. Celkově bezpečnost stojí na správných Symfony primitivech — viditelné problémy z dokumentace nejsou.]
Souhlasím. 

**O6.** Poster — čitelný, přenese hodnotu?
> [Návrh: Poster existuje jako PNG soubor (Poster-Kotlas.png). Grafiku a čitelnost nemohu plně posoudit — toto musíš vyhodnotit ty.]
Duster j spíše. Err jednodušší. Err. Staré logo školy. Err a některé bloky. Mu ho působit, že jsou tak jako naskládané vedle sebe docela náhodně s různými odstupy, například odstup od pravého okraje tam je nejasný. A je to takový poslepovaný z. Aj aj generovaných diagramů, což nemusí být nutně špatně, ale nemá to úp. Nepůsobí to úplně jednotně. Takže v tomhle smyslu je poster spíše nižší kvality? Každopádně, co se týče těch informací, který jako sděluje, tak ty jsou v pohodě. Co mi v Polsku chybí, tak je nějaký jasný screenshot. Z té aplikace minimálně 2, protože ta aplikace je jako velmi hezká AA měla testovací data, takže to tam mohlo bejt daný

**O7.** Je systém reálně nasazený u nějaké firmy, nebo je to ukázka?
> [Návrh: Deployment guide pro VPS existuje (DEPLOYMENT.md), Docker Compose je připravený pro produkci. Zda systém běží u reálné firmy, musíš potvrdit ty — z dostupných materiálů to není zřejmé.]
Systém byl v reálném nasazený deployment byl provedený na virtual. Právě server na to proběhlo pilotní testování i zástupci té firmy. Následné nasazení dodal, do provozu je odloženo z důvodu přetížení té firmy reálnými projekty, které mají vyšší prioritu a změny vedení. Následně se tato. Možnost nově otevře, případně je tam ještě varianta, že se systém mírně upraví a bude se pasovat na jinou firmu, což by si autor potom sám. Err řešil. Takže takhle to to je aktuální situace.  

---

## 5) Adam Mikulič — *Komunikační modul pro bezpilotní letoun*

### Vedoucí

**V1.** Průběh — hardware + firmware.
> [Toto musíš vyhodnotit ty z osobní zkušenosti a konzultací.]
Student měl zadání nad rámec toho, co se učí ve škole. To znamená, že učitel se už velké množství věcí sám protokoly vlastní debugovací aplikace, dělání vlastních obvodů a takže. Na konzultacích spíše reportoval, ale problémy řešil velmi samostatně, takže super.  

**V2.** Spolupráce s Joly (letoun nese modul) — koordinace rozhraní, hmotnost, napájení?
> [Toto musíš vyhodnotit ty. Z technické stránky: Mikuličova dokumentace explicitně popisuje napájecí rozsah modulu 5–8,4 V (2S LiPo) a hmotnostní limity jsou klíčové pro letoun s 250g payloadem. Mikuličův README zmiňuje "reálné testování" dosahu s přibližně 2× zlepšením — to předpokládá skutečnou integraci s Jolym.]
Ano. Testování proběhlo zeptat se. Možná na obhajobě, jestli zkoušeli jako třeba bez toho letu, ale jestli zkoušeli nějakou reakci na to, když to dali opravdu na obrovskou vzdálenost. Nebo jestli? To bylo z čeho tak usuzuješ. A ten pilot tam určitě měl, je to je v pohodě a spolupráce byla kvalitní.  

**V3.** Největší technické překážky (anténa, RF, firmware, integrace).
> [Toto musíš vyhodnotit ty. Z dokumentace jsou viditelné netriviální technické problémy, které musel vyřešit: (1) Half-duplex/full-duplex konverze CRSF signálu — potřeboval vlastní PCB s SN74HC125DR quad buffer IC v KiCadu. (2) Rozdílné baud rates na dvou UARTech (420 000 baud pro receiver vs. 400 000 baud pro JR-bay). (3) Invertovaný signál pro JR-bay port. (4) Dual-core task management na ESP32 (Core 1 pro radio, Core 0 pro WiFi). To jsou skutečné embedded systémové problémy, ne jen copy-paste.]
Technickými problémy bylo správné nastavení těch protokolů a celkově vyřešení veškerého zapojení vytvoření vlastního debugovací ho systému. Um. Tam ty rozdílný body. Pravděpodobně to tam bylo taky hustý programování v céčku. Err Takže hodně hodně věcí tam bylo. Tam píšeš to líp než já jo reálně. 



**V4.** Reálné měření doletu — udělal ho, jak, s jakými výsledky?
> [Návrh: README explicitně uvádí "relay node přibližně zdvojnásobil efektivní komunikační dosah v reálném testování". Dashboard monitoruje RSSI (dBm), Link Quality (%) a SNR v reálném čase. Konkrétní vzdálenosti a metodiku měření (kde, jak, s jakým referenčním řešením) musíš ověřit ty z článku nebo osobní zkušenosti.]
Reálný měření. Err, nevím jistě, jestli bylo ale test v reálným prostoru určitě bylo.  

**V5.** Silné a slabé stránky studenta.
> [Toto musíš vyhodnotit ty. Technicky viditelné silné stránky: vlastní PCB design v KiCadu, C++ firmware pro embedded ESP32, pochopení CRSF protokolu (CRC-8, frame struktura, timing), reálné field testy. 426 řádků firmware kódu s dual-core managementem — solidní embedded práce.]
Zase silnou stránkou studenta je samostatnost schopnost postavit se velkému problému, který je nad rámec. Kombinace hardware a software skillu. Firmware věcí err. Pájení. Vytvoření vlastního obvodu Pro pochopení ASP. Takže strašně moc věcí tam je.   Slabou stránkou je. Prezentování a schopnost vysvětlit schopnost prodat svojí činnost a tam věřím, že to dokáže na obhajobě velmi zlepšit.  

### Oponent

**O1.** Splnění zadání — "rozšíření dosahu komunikace". O kolik se dosah prokazatelně zvýšil a jak to bylo měřeno?
> [Návrh: README deklaruje ~2× zlepšení efektivního komunikačního dosahu v reálném testování. Dashboard monitoruje RSSI, LQ, SNR — měřitelné metriky existují. Konkrétní čísla (např. z X m na Y m), podmínky měření a srovnání s referenčním stavem (bez relay) musíš ověřit ty z článku. Bez těchto čísel je deklarace "2×" obtížně obhajitelná před komisí.]
Vzdálenost rádiového přenosu ověřena byla ovšem ne v plném zapojení s letadlem. Místo letadla bylo auto s notebookem a příjimačem. Jeden stál na místě a hýbal s ovladačem a druhý jel v autě dokud nezažil node signál, pak zacouval, položil node tak aby zase měl signál a jel dál dokud přijímač neztratil signál, tak byla ověřena vzdálenost přenosu. Jelikož v testu chceme být na hraně ztráty signálu, zkoušet to s letadlem by bylo velmi nezodpovědné --



**O2.** Článek — metodika měření, referenční srovnání s běžnými řešeními, limity.
> [Návrh: PDF článek existuje. Zadání vyžadovalo: analýzu komunikačních systémů, návrh řešení, HW/SW implementaci, výsledky testování. Obsah PDF nemohu přečíst — toto musíš vyhodnotit ty. Klíčové: jsou tam konkrétní naměřené hodnoty se srovnávací metodikou?]
No metodika byla dobrá Dobře to vyhodnotili a. Konkrétní na měření hodnoty prezentovaly. Primárně formou videa.  

**O3.** Technická dokumentace (MD + rozšířený web `site/`) — stačí ke stavbě druhého kusu?
> [Návrh: Legacy dokumentace má 587 řádků + MkDocs site struktura. Pokrývá: kompletní GPIO pinout s napěťovými úrovněmi ✓, CRSF frame struktura s CRC-8 ✓, UART konfigurace (420k/400k baud, invertovaný signál) ✓, 3 API endpointy s JSON schématy ✓, PCB design (KiCad soubory) ✓, build a flash instrukce ✓, troubleshooting (6 scénářů) ✓. Pro stavbu druhého kusu by dokumentace měla stačit — KiCad soubory pro PCB jsou v repozitáři.]
 

**O4.** Kvalita prezentace (PPTX / PDF) — obsah, přiměřenost času obhajoby.
> [Návrh: Odevzdán PPTX originál + PDF konverze. Obsah prezentace nemohu přečíst (PPTX/PDF) — toto musíš vyhodnotit ty.]
Prezentace obsahuje ještě podstatný, není to sice úplně designově zázrak, ale myslím si, že bude účinná.

**O5.** Poster — grafika a obsah.
> [Návrh: PDF poster existuje. Grafiku a obsah nemohu vyhodnotit — toto musíš posoudit ty.]
Polstr je přehledný, obsahuje vše podstatné a. Je i graficky err v rámci možnosti hezký 


**O6.** Je modul integrován a fungoval s Jolyho letounem v ostrém testu, nebo jen odděleně na stole?
> [Návrh: README Mikuliče zmiňuje "reálné testování" s dosahovou metrikou — to naznačuje integraci s letounem, ne jen stolní test. Joly odevzdal videa letů (Google Drive). Zda je modul viditelně na palubě ve videích a zda komunikace fungovala za letu, musíš ověřit ty z videí nebo osobní zkušenosti.]
Ano modul byl implementován přímo v ostrém testu, vlastně ten test trail test funguje čistě přes ten modul, není tam přepínání, že bez modulu pro modul, takže vždycky, kdy tyto letadlo letělo, takhle to laskavě ten modul. To jsou vám metrika? Byla err testována z důvodu bezpečnosti bez letícího modulu ta letícího letounu to znamená. Tak to bylo zmíněný nahoře.  

---

## Poznámky (libovolné)

Sem klidně nadiktuj cokoli dalšího — celkový dojem z ročníku, srovnání studentů, obecné principy, na kterých chceš trvat v obou posudcích, apod.

>
