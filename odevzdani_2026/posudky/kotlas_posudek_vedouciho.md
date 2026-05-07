# Posudek vedoucího maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Jiří Kotlas |
| Téma práce | Project Manager – systém na řízení firemních procesů a dokumentů |
| Vedoucí práce | Ing. Adam Ferencz |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Průběh práce a spolupráce se studentem

Student nastoupil k projektu v situaci, kdy musel framework Symfony i celý ekosystém PHP aplikací studovat zcela od základů. Přesto pracoval v dobrém tempu a harmonogram práce v zásadě dodržoval. Fakt, že zvládl realizovat projekt s takovou architektonickou komplexností bez předchozí zkušenosti s použitými technologiemi, svědčí o jeho cílevědomosti a schopnosti učit se pod reálným tlakem.

Konzultace probíhaly průběžně a konstruktivně. Student konzultoval jak s vedoucím práce, tak s reálným klientem – zástupci firmy, pro niž byl systém navrhován. Tuto schopnost komunikovat se zadavatelem a překlídat jeho požadavky do konkrétní podoby aplikace hodnotím jako mimořádně zralý přístup.

## 2. Míra samostatnosti

Student nepotřeboval výraznou pomoc při architektonických rozhodnutích – volba Symfony 7.4, Doctrine ORM s Voter pattern pro řízení přístupu a Docker pro nasazení jsou zralá a dobře odůvodněná rozhodnutí, která nevypadají jako výsledek náhodné asistence, ale jako informovaná volba člověka, který tématu rozumí. Celý systém byl navržen s ohledem na reálné nasazení ve firemním prostředí.

## 3. Plnění zadání

Systém splňuje všechny požadavky zadání s přidanou hodnotou. Implementovány jsou CRUD operace pro všechny moduly (klienti, projekty, nabídky, objednávky, smlouvy, akceptační protokoly, faktury), řízení přístupu s Voter třídami pro 3 role, dashboard s KPI, reporty s grafy (Chart.js) a 9 stavových workflow. Systém byl nasazen na VPS a proběhlo pilotní testování se zástupci firmy.

Rozsah projektu (22 Doctrine entit, 14 controllerů, 60 Twig šablon, 35+ tras, 16 migrací) je objektivně nadprůměrný a zároveň funkčně provázaný – nejde o nafouknutý scope, ale o systém, který zachycuje reálný firemní proces end-to-end.

## 4. Hodnocení výstupů

**Článek:** Výborný – velmi podrobný, přítomny přehledy a diagramy, které jsou přínosné. Drobná formální výtka: v článku chybí povinný úvodní obrázek. Diagramy by mohly zabírat oba sloupce, čímž by získaly na čitelnosti.

**Technická dokumentace:** Nejkompletnější dokumentace v celém ročníku – 1 111 řádků. Pokrývá deployment na VPS (DEPLOYMENT.md), datový model všech 22 entit, ACL model s popisem Voter tříd, 35+ tras, fixture data s realistickými testovacími sadami a 10 troubleshootingových scénářů. Nasazení systému z dokumentace by mělo být plně reprodukovatelné.

**Poster:** Informačně postačující, ale graficky slabší. Používá staré logo školy, rozložení bloků působí nesourodě a chybí screenshoty aplikace, která je designově zdařilá a měla by být na posteru viditelně prezentována.

## 5. Silné stránky a rezervy

**Silné stránky:** Cílevědomost, schopnost zvládnout enterprise technologie zcela samostatně, práce s reálným klientem, výjimečná dokumentace, ambice realizovat projekt s reálnou hodnotou.

**Rezervy:** Grafická reprezentace práce (poster) neodpovídá kvalitě samotné aplikace. Pokrytí unit testy je deklarováno jako průběžně rozšiřované – konkrétní rozsah bude vhodné objasnit na obhajobě.

## 6. Navrhovaná klasifikace

Jiří Kotlas odvedl výjimečný výkon. Realizoval komplexní podnikový informační systém od návrhu po pilotní nasazení u reálného klienta, přičemž všechny použité technologie musel zvládnout od základů. Jde o nejambicióznější softwarový projekt ročníku.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Ing. Adam Ferencz, vedoucí maturitní práce*
*Gymnázium Havlíčkův Brod, 5. 5. 2026*
