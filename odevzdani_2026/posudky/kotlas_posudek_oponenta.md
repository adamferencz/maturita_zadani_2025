# Posudek oponenta maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Jiří Kotlas |
| Téma práce | Project Manager – systém na řízení firemních procesů a dokumentů |
| Oponent práce | Mgr. Jiří Rojka |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Splnění funkčních požadavků zadání

Systém prokazatelně splňuje všechny funkční požadavky zadání a v řadě aspektů je přesahuje. Jsou implementovány:

- Kompletní CRUD pro všechny moduly: klienti, projekty, nabídky, objednávky, smlouvy, akceptační protokoly, faktury.
- Řízení přístupu (ACL) s 3 Voter třídami a rolovou hierarchií.
- Dashboard s KPI metrikami.
- Reporty s interaktivními grafy (Chart.js).
- Stavová workflow pro 9 typů dokumentů.
- E-mailové notifikace.
- Bezpečné nahrávání souborů mimo webroot.
- Reset hesel.

Systém byl nasazen na VPS a proběhlo pilotní testování se zástupci reálné firmy, pro niž byl systém zamýšlen.

## 2. Odborná úroveň a kvalita zpracování

Projekt je na výjimečné technické úrovni. Architektura odpovídá komerčnímu podnikovému softwaru: 22 Doctrine entit s komplexními vazbami, 14 controllerů, 13 formulářových typů, 60 Twig šablon, 16 databázových migrací, 35+ tras a 9 stavových workflow. Business flow systému – klienti → projekty → nabídky → objednávky → smlouvy → akceptační protokoly → faktury – je logicky provázaný a funkční jako celek.

Bezpečnostní architektura stojí na standardních Symfony primitivech: Doctrine ORM s parametrizovanými dotazy (ochrana před SQL injection), CSRF tokeny v Symfony formulářích, upload mimo webroot a Voter pattern pro fine-grained řízení přístupu. Implementace je prokazatelně bezpečná.

## 3. Formální zpracování

**Článek:** Výborný – podrobný, obsahuje diagramy a přehledy, které jsou přínosné pro pochopení architektury. Formální výtka: chybí povinný úvodní obrázek, který je standardní součástí odborných článků. Diagramy by mohly být sazeny přes oba sloupce pro lepší čitelnost.

**Technická dokumentace:** Nejrozsáhlejší ze všech posuzovaných projektů (1 111 řádků). Pokrývá kompletní deployment na VPS, datový model všech 22 entit, ACL model, routing, fixture data a troubleshooting. Reprodukovatelnost systému z dokumentace hodnotím jako výbornou.

**Poster:** Informačně postačující – sděluje účel a fungování systému. Grafická kvalita je nižší: použito je staré logo školy, rozmístění bloků působí nesourodě a chybí screenshoty aplikace. Systém má výrazné, přehledné uživatelské rozhraní, které by na posteru přitáhlo pozornost komise.

## 4. Otázky k obhajobě

1. Dokumentace zmiňuje PHPUnit testy jako „průběžně rozšiřované". Kolik testů je aktuálně implementováno a jaké části systému pokrývají? Jak byste ohodnotil celkové testovací pokrytí?
2. Jak konkrétně pracuje Voter pattern při ověřování přístupu? Popište tok požadavku od klienta po rozhodnutí Voteru na konkrétním příkladu (např. úprava faktury jiným uživatelem, než kdo ji vytvořil).
3. Systém byl pilotně testován se zástupci firmy. Jaká zpětná vazba z pilotního provozu vzešla a co byste na základě ní případně změnil?

## 5. Navrhovaná klasifikace

Projekt je ukázkovým příkladem ambiciózního, technicky zvládnutého a reálně nasazeného podnikového systému. Architektonická zralost, rozsah funkcionality a kvalita dokumentace výrazně přesahují standardní požadavky maturitní práce.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Mgr. Jiří Rojka, oponent maturitní práce*
*5. 5. 2026*
