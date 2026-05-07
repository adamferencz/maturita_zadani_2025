# Posudek vedoucího maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Adam Mikulič |
| Téma práce | Komunikační modul pro bezpilotní letoun |
| Vedoucí práce | Ing. Adam Ferencz |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Průběh práce a spolupráce se studentem

Student si vybral zadání, které výrazně přesahuje rozsah látky probírané ve škole. Musel se samostatně naučit bezdrátové komunikační protokoly (CRSF), návrh desek plošných spojů v KiCadu, programování embedded systémů v C++ a integraci WiFi komunikace na ESP32. Na konzultacích student spíše reportoval o dosažených výsledcích než hledal pomoc s překonáváním problémů – naprostou většinu technických překážek identifikoval a vyřešil bez přímé asistence vedoucího práce. Tento přístup hodnotím jako výjimečný.

## 2. Míra samostatnosti

Projekt byl realizován s mimořádnou mírou samostatnosti. Student zvládl průnik hardware a firmware dovedností – od pájení elektroniky a vytváření vlastního PCB po psaní C++ firmware s dual-core task managementem na ESP32. Vytvořil si vlastní debugovací aplikaci, aby mohl efektivně diagnostikovat problémy v komunikačním stacku. Spolupráce s Jolym při integraci modulu na letoun proběhla bez nutnosti zprostředkování vedoucím.

## 3. Plnění zadání

Komunikační modul byl navržen, vyroben a otestován. Dosah bezdrátového přenosu byl prokazatelně zvýšen – testování proběhlo prakticky na pozemních vozidlech (auto s přijímačem pohybující se až na hranici ztráty signálu), přičemž tato metodika je z hlediska bezpečnosti pro letecký provoz zcela správná. Modul byl posléze integrován přímo na palubu Jolyho letounu a komunikace za letu probíhala výhradně přes tento modul.

Projekt splnil zadání a přinesl funkční, reálně otestovaný výstup s měřitelným zlepšením komunikačního dosahu.

## 4. Hodnocení výstupů

**Článek:** Kvalitní, s dobrou metodikou testování. Konkrétní naměřené hodnoty dosahu jsou prezentovány, mj. formou videa.

**Technická dokumentace:** Komplexní dokumentace (587 řádků + MkDocs webová struktura) pokrývá GPIO pinout, CRSF frame strukturu, UART konfiguraci, API endpointy, PCB design a build instrukce. Spolu s přiloženými KiCad soubory by dokumentace umožnila stavbu druhého kusu.

**Prezentace:** Obsahuje vše podstatné, po designové stránce není výtvarně přepychová, ale bude věcně účinná.

**Poster:** Přehledný, obsahuje vše podstatné, graficky v rámci svých možností zdařilý.

## 5. Silné stránky a rezervy

**Silné stránky:** Mimořádná samostatnost, schopnost postavit se technickému problému daleko přesahujícímu gymnaziální osnovy, kombinace hardware a software dovedností (PCB design, pájení, C++ firmware, embedded systémy, bezdrátové protokoly).

**Rezervy:** Schopnost prezentovat a „prodat" svoji práci laické publiku. Student je zdatný technolog, ale komunikace výsledků navenek mu jde méně přirozeně – věřím, že na obhajobě tuto rezervu výrazně zmenší.

## 6. Navrhovaná klasifikace

Adam Mikulič realizoval projekt výjimečné technické náročnosti, který by byl výzvou i pro studenty vysokých technických škol. Výsledný modul fyzicky funguje, byl otestován v reálném prostředí a integrován s Jolyho letounem. Práce přesahuje rámec gymnazijní maturitní práce.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Ing. Adam Ferencz, vedoucí maturitní práce*
*Gymnázium Havlíčkův Brod, 5. 5. 2026*
