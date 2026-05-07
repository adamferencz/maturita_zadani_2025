# Posudek vedoucího maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Josef Holeček |
| Téma práce | Webový portál pro kroužky a trenéry v Havlíčkově Brodě |
| Vedoucí práce | Ing. Adam Ferencz |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Průběh práce a spolupráce se studentem

Student pracoval po celý školní rok průběžně a s dostatečnou aktivitou. Projekt realizoval od počátečního návrhu architektury až po nasazení na produkční cloudovou infrastrukturu, a to přesto, že všechny použité technologie (React, Firebase, Vercel) musel studovat zcela od základů. Prokázal schopnost samostatně se vypořádat i s nečekanými technickými překážkami – například se situací spojenou s registrací placené cloudové služby, která by mnohé studenty odradila.

Konzultace probíhaly pravidelně v rámci vyučovacích hodin, student zpětnou vazbu přijímal konstruktivně a promítal ji do dalšího vývoje. V závěru projektu bylo zapotřebí jej mírně motivovat k doplnění reálných dat a k dotažení aplikace do stavu vhodného pro veřejné nasazení.

## 2. Míra samostatnosti

Přibližně 95 % technických problémů student vyřešil bez přímé intervence vedoucího. Vedoucí práce poskytoval zejména motivaci a obecný teoretický rámec, který byl z větší části součástí standardní výuky. Student efektivně využíval AI nástroje jako podpůrný prostředek vývoje, na což se jako na moderní pracovní styl dívám kladně.

## 3. Plnění zadání

Aplikace splňuje funkční rozsah zadání: veřejný katalog kroužků s filtrováním podle věku, kategorie a lokality, profily trenérů se správou kroužků a administrátorský panel pro schvalování obsahu. Aplikace je nasazena na produkční infrastruktuře (Vercel + Firebase). Trenéři v omezené míře skutečně vyplňovali své profily a kroužky. Funkci registrace ze strany rodičů ověřil student testováním na zkušebních datech.

Za zásadní slabinu celé práce považuji skutečnost, že aplikace nebyla zveřejněna pro reálné rodiče a nebyla v ostrém provozu ověřena koncovými uživateli. Přestože se jedná spíše o organizační než technický nedostatek, tato okolnost výrazně snižuje praktický dopad jinak technicky dobře zpracovaného projektu. Zadání explicitně požadovalo nasazení do reálného provozu a zpětnou vazbu od komunity.

## 4. Hodnocení výstupů

**Článek:** Splňuje požadavky zadání po stránce struktury i obsahové kvality. Text je čtivý, srozumitelný a dostatečně odborný.

**Technická dokumentace:** Dokumentace čítá přes 1 000 řádků a je velmi komplexní – pokrývá přehled systému, tech stack, strukturu repozitáře, databázové schéma, autentizaci, routing i deployment na Vercel. Cizí vývojář by byl schopen projekt podle ní zprovoznit. Formálně chybí vyplněné README v kořenovém adresáři projektu. Doporučuji studenta na obhajobě dotázat na aktuální stav Firestore security rules.

**Poster:** Graficky pěkně zpracovaný, přehledný a čitelný i pro laické publikum.

## 5. Silné stránky a rezervy

**Silné stránky:** Prokazatelná samostatnost, schopnost učit se nové technologie za provozu, efektivní práce s AI nástroji, designově kvalitní aplikace.

**Rezervy:** Dotahování projektů do finálního stavu, zejména zapojení reálných uživatelů. V případě závažnějšího výpadku by mohla být limitující závislost na AI nástrojích bez hlubšího porozumění použitých technologií.

## 6. Navrhovaná klasifikace

Práce je technicky zdařilá a student prokázal schopnost realizovat komplexní webový projekt od návrhu po nasazení v cloudu. Absenci plného spuštění aplikace do ostrého provozu a ověření u reálných koncových uživatelů (rodičů) však považuji za podstatné nenaplnění jednoho z klíčových požadavků zadání, které navrhovanou klasifikaci snižuje.

**Navrhuji klasifikaci: 2 – chvalitebný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Ing. Adam Ferencz, vedoucí maturitní práce*
*Gymnázium Havlíčkův Brod, 5. 5. 2026*
