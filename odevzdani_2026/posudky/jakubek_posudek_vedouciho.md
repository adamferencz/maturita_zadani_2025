# Posudek vedoucího maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Jakub Jakůbek |
| Téma práce | Webová aplikace pro distribuci školních propagačních předmětů (GHB Merch) |
| Vedoucí práce | Ing. Adam Ferencz |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Průběh práce a spolupráce se studentem

Student pracoval po celý rok v zásadě samostatně a svůj projekt dotáhl do pokročilého stádia připravenosti pro provoz. V průběhu roku bylo v některých fázích potřeba jej motivovat k řešení komplexnějších prvků, které by jinak pravděpodobně dočasně odložil. Právě toto popostrčení mělo pozitivní vliv na výslednou úroveň projektu.

Konzultace probíhaly průběžně a student reagoval na zpětnou vazbu. Schůzky s potenciálním administrátorem systému (zástupcem školy jako klienta) si student sjednával a vedl zcela samostatně, což svědčí o jeho schopnosti komunikovat s reálným zadavatelem a překládat jeho potřeby do konkrétních funkčních požadavků.

## 2. Míra samostatnosti a přístup k zadání

Student přistoupil k projektu proaktivně: sám zmapoval reálné potřeby školy, navrhl způsoby řešení, které zadavatele samy nenapadly, a do implementace přinesl technická rozhodnutí s přidanou hodnotou (např. HMAC validace QR kódů pro výdej nebo integrace Microsoft SSO pro školní účty). Aktivně využíval moderní přístupy vývoje včetně AI asistence.

## 3. Plnění zadání

Aplikace splňuje všechny funkční požadavky zadání: katalog produktů s barevnými a velikostními variantami, hromadný objednávkový systém s minimálními množstvími, tři uživatelské role (uživatel, admin, superadmin), QR kódy pro výdej s HMAC ověřením, administrátorský panel se sledováním životního cyklu objednávek, reportingový dashboard a integrace Microsoft SSO pro přihlášení přes @ghb.cz účty. Aplikace je nasazena na vlastní doméně s platným HTTPS.

Aplikací v rámci testování prošla celá třída, což cením jako nadstandardní přístup k ověření funkčnosti. Slabinou zůstává, že výdejky nebyly dosud spuštěny v ostrém provozu – škola pro projekt pořizuje hosting a pravděpodobně dojde k finálnímu nasazení ještě před maturitami.

## 4. Hodnocení výstupů

**Článek:** Dostatečně kvalitní a dobře strukturovaný, obsahuje vše podstatné. Jako drobný nedostatek vnímám, že administrátorské rozhraní, které je technicky i designově velmi propracované, je v článku popsáno a vizuálně zdokumentováno nedostatečně.

**Technická dokumentace:** Dokumentace o rozsahu přibližně 800 řádků je jedna z nejpropracovanějších v ročníku. Pokrývá kompletní databázové schéma, API endpointy, routing, e-mailový systém i deployment přes Docker. Hodnocení je výborné.

**Poster:** Přehledný a srozumitelný. Bylo by přínosné zahrnout více screenshotů aplikace, aby charakter projektu vynikl na první pohled.

## 5. Silné stránky a rezervy

**Silné stránky:** Zkušenost s end-to-end návrhem reálného produktu, schopnost vymýšlet chytrá technická řešení, proaktivní práce s klientem, moderní technologický stack (SvelteKit 5, PostgreSQL, Docker, vlastní produkční nasazení).

**Rezervy:** Občasné nedodržení dílčích termínů. Student má mimořádné technické schopnosti, ale ne vždy jim věnuje odpovídající důraz – v některých momentech mohl výsledek práce více reprezentovat.

## 6. Navrhovaná klasifikace

Student odvedl výjimečný výkon: realizoval komplexní, technicky sofistikovaný projekt s reálnou hodnotou pro školu, s pokročilou bezpečnostní architekturou a moderním produkčním nasazením. Přes dílčí nedostatky v dotažení do ostrého provozu jde o jednu z nejsilnějších prací ročníku.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Ing. Adam Ferencz, vedoucí maturitní práce*
*Gymnázium Havlíčkův Brod, 5. 5. 2026*
