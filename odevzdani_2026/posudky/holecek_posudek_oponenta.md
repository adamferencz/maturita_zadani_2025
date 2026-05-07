# Posudek oponenta maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Josef Holeček |
| Téma práce | Webový portál pro kroužky a trenéry v Havlíčkově Brodě |
| Oponent práce | RNDr. Jaroslav Kocman |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Splnění funkčních požadavků zadání

Portál prokazatelně splňuje všechny funkční požadavky: veřejný katalog kroužků s filtrováním podle věku, kategorie a lokality, profily trenérů se správou vlastních kroužků, administrátorský panel pro schvalování a zamítání příspěvků a responzivní design pro mobilní zařízení. Databáze pracuje v reálném čase prostřednictvím Firebase Firestore. Aplikace je nasazena na produkční infrastruktuře Vercel + Firebase, nikoli pouze lokálně.

Upozorňuji, že z dokumentace vyplývá, že Firestore security rules byly v průběhu vývoje záměrně nastaveny permisivně (`allow create, update, delete: if true`). Doporučuji objasnit, zda jsou tato pravidla v produkčním prostředí opravena.

## 2. Odborná úroveň a kvalita zpracování

Projekt představuje technicky kompetentní řešení pro reálnou komunitu. Volba technologického stacku (React, Firebase, Vercel) je vhodná pro daný typ aplikace a odpovídá moderní praxi vývoje webových aplikací. Student zvládl implementaci autentizace, real-time databáze i cloudového nasazení, což jsou oblasti vyžadující netriviální znalosti.

Hlavní limitací zůstává absence ověřené uživatelské přijatelnosti. Aplikace nebyla zveřejněna pro reálné rodiče, přestože technická infrastruktura je pro ostrý provoz připravená. Uživatelská použitelnost portálu tak nebyla v reálném prostředí verifikována.

## 3. Formální zpracování

**Článek:** Splňuje požadavky zadání po stránce struktury i obsahu. Práce je srozumitelná a dostatečně odborná.

**Technická dokumentace:** Rozsáhlá a komplexní dokumentace (přes 1 000 řádků) pokrývá celý systém od instalace přes databázové schéma po deployment. Hodnocení je kladné. Poznámka: README kořenového adresáře projektu obsahuje nevyplněné placeholdery.

**Poster:** Graficky pěkně zpracovaný, přehledný a srozumitelný i pro laické publikum. Obsahuje klíčové informace o projektu.

## 4. Otázky k obhajobě

1. V dokumentaci jsou Firestore security rules popsány jako dočasně nastavené permisivně pro potřeby vývoje. Jsou v současné produkční verzi opraveny? Jaká pravidla jsou aktuálně nastavena a jak chrání data uživatelů?
2. Co konkrétně bránilo tomu, aby byl portál zveřejněn a zpřístupněn i rodičům? Plánujete po maturitě aplikaci uvést do plného provozu?
3. Jak byste z hlediska UX a datové dostupnosti řešili situaci, kdy by rodič hledal kroužek ve svém okolí, ale katalog by pro danou lokalitu neobsahoval žádné záznamy?

## 5. Navrhovaná klasifikace

Práce prokazuje solidní technické zvládnutí moderního webového vývoje. Nasazení na cloudové infrastruktuře a reálná účast trenérů jsou pozitivní aspekty. Absence plného veřejného spuštění a uživatelského testování s reálnými rodiči je limitem, jehož kontext je vhodné objasnit na obhajobě.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*RNDr. Jaroslav Kocman, oponent maturitní práce*
*5. 5. 2026*
