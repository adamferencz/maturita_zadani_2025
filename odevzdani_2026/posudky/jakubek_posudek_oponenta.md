# Posudek oponenta maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Jakub Jakůbek |
| Téma práce | Webová aplikace pro distribuci školních propagačních předmětů (GHB Merch) |
| Oponent práce | Mgr. Aleš Novák |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Splnění funkčních požadavků zadání

Aplikace splňuje veškeré funkční požadavky zadání: katalog produktů s barevnými a velikostními variantami, hromadný objednávkový systém s minimálními množstvími, správa tří uživatelských rolí (user / admin / superadmin), QR kódy pro výdej s HMAC ověřením, administrátorský panel se sledováním životního cyklu objednávek ve 5 stavech (pending\_batch → processing → ready → completed / cancelled), statistický a reportingový dashboard, integrace Microsoft SSO pro přihlašování přes školní účty @ghb.cz a automatické e-mailové notifikace. Všechny klíčové moduly jsou prokazatelně implementovány.

## 2. Odborná úroveň a kvalita zpracování

Projekt je technicky na velmi vysoké úrovni pro maturitní práci. Volba SvelteKit 5 s Runes API (vydáno říjen 2024) svědčí o sledování aktuálního vývoje oboru a ochotě pracovat s cutting-edge technologiemi. Vlastní produkční deployment s Docker Compose a automatickým HTTPS přes Caddy, HMAC validace QR kódů a httpOnly cookies s rate limitingem jsou opatření, která by obstála i v komerčním prostředí.

Aplikace úspěšně prošla testováním s celou třídou jako uživateli, což je neobvyklý a chvályhodný přístup k ověření funkčnosti. Slabinou zůstává, že k reálnému ostrovnímu provozu s ostrými objednávkami a výdeji dosud nedošlo.

## 3. Formální zpracování

**Článek:** Dostatečně kvalitní, dobře strukturovaný a přiměřeně dlouhý. Obsahuje vše podstatné. Slabinou je nedostatečné vizuální zdokumentování administrátorského rozhraní – administrátorská část je technicky propracovaná, ale v článku není dostatečně pokryta screenshoty ani popisem.

**Technická dokumentace:** Komplexní dokumentace (~800 řádků) pokrývá kompletní databázové schéma s 8 hlavními tabulkami, 14+ API endpointů s příklady požadavků a odpovědí, routing, e-mailový systém, zpracování obrázků i kompletní deployment přes Docker. Hodnocení je výborné.

**Poster:** Přehledný a srozumitelný. Obsahuje klíčové informace o projektu. Pro lepší prezentaci povahy aplikace by bylo přínosné zahrnout více screenshotů uživatelského i administrátorského rozhraní.

## 4. Otázky k obhajobě

1. Jak přesně funguje HMAC validace QR kódů při výdeji? Co by se stalo, kdyby někdo QR kód zkopíroval a pokusil se jej použít vícekrát nebo na jiném výdejním místě?
2. Aplikaci testovala celá třída, ale reálné výdejky dosud neproběhly. Jaké konkrétní scénáře byste očekávali v ostrém provozu, které testování nemohlo odhalit?
3. Microsoft SSO umožňuje přihlášení přes @ghb.cz účty – jak se aplikace zachová při pokusu o přihlášení s účtem mimo tuto doménu? Je toto ošetřeno na úrovni aplikace, nebo pouze na straně Azure AD?

## 5. Navrhovaná klasifikace

Projekt je technicky mimořádně zdařilý – moderní fullstack architektura, pokročilá bezpečnostní opatření, propracovaný deployment a reálná hodnota pro školu. Jde o výjimečný výstup v kontextu maturitní práce.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Mgr. Aleš Novák, oponent maturitní práce*
*5. 5. 2026*
