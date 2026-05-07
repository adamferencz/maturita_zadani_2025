# Posudek oponenta maturitní práce

| Položka | Údaj |
|---|---|
| Škola | Gymnázium Havlíčkův Brod |
| Školní rok | 2025/2026 |
| Autor práce | Adam Mikulič |
| Téma práce | Komunikační modul pro bezpilotní letoun |
| Oponent práce | Mgr. Aleš Novák |
| Datum vypracování posudku | 5. 5. 2026 |

---

## 1. Splnění požadavků zadání

Zadání požadovalo návrh a realizaci komunikačního modulu rozšiřujícího dosah rádiové komunikace bezpilotního letounu. Tento požadavek je prokazatelně splněn:

- Modul byl fyzicky vyroben včetně vlastního PCB designu v KiCadu.
- Byl implementován firmware pro ESP32 v C++ s dual-core architekturou.
- Dosah bezdrátového přenosu byl měřen reálným terénním testem: přijímač na autu pohybujícím se od operátora s ovladačem, přičemž bylo určeno místo ztráty signálu bez relay uzlu a s relay uzlem. Tato metodika je bezpečná a věrohodná.
- Modul byl integrován na palubu Jolyho letounu a komunikace za skutečného letu probíhala výhradně přes tento modul.
- Reálné testování dosahu bez letounu (s autem) je metodicky správnou volbou – testovat hranici dosahu s letícím letounem by bylo nezodpovědné.

## 2. Odborná úroveň a kvalita zpracování

Projekt je technicky na mimořádně vysoké úrovni. Student zvládl průnik oborů, který je netriviální i pro zkušeného embedded vývojáře:

- **Návrh PCB** v KiCadu se SN74HC125DR quad buffer IC pro half-duplex/full-duplex konverzi CRSF signálu.
- **Firmware** v C++ s dual-core task managementem na ESP32 (Core 1 pro rádiový stack, Core 0 pro WiFi).
- **Protokolová vrstva**: CRSF protokol s CRC-8 kontrolou integrity, řešení rozdílných přenosových rychlostí (420 000 baud pro přijímač vs. 400 000 baud pro JR-bay port) a invertovaného signálu.
- **Webový dashboard** pro real-time monitoring RSSI, Link Quality a SNR.
- **Vlastní debugovací aplikace** pro diagnostiku komunikačního stacku.

Toto jsou skutečné embedded systémové problémy, jejichž řešení vyžaduje hlubokou technickou znalost.

## 3. Formální zpracování

**Článek:** Kvalitní odborný text s dobrou metodikou. Konkrétní naměřené hodnoty dosahu jsou přítomny, mj. prezentovány formou videa. Metodika srovnání s referenčním stavem (bez relay / s relay) je popsána věrohodně.

**Technická dokumentace:** Komplexní dokumentace (587 řádků legacy MD + MkDocs webová struktura) pokrývá: kompletní GPIO pinout s napěťovými úrovněmi, CRSF frame strukturu s CRC-8, UART konfiguraci, 3 API endpointy, PCB design (KiCad soubory přiloženy), build a flash instrukce a 6 troubleshootingových scénářů. Dokumentace by umožnila stavbu druhého kusu.

**Prezentace:** Obsahuje vše podstatné. Není výtvarně přepychová, ale bude věcně účinná.

**Poster:** Přehledný, obsahuje vše podstatné a graficky zdařilý.

## 4. Otázky k obhajobě

1. Popište přesně terénní test dosahu: jaká byla vzdálenost bez relay uzlu a jaká s relay uzlem? Za jakých podmínek probíhalo měření (přímá viditelnost, terén, výkon vysílače)? Jaké konkrétní číselné hodnoty dosahu jste naměřili?
2. Co přesně dělá SN74HC125DR quad buffer IC ve vašem PCB designu a proč byl nezbytný? Jaký problém by nastal bez něj?
3. Jak jste řešili synchronizaci komunikace mezi dvěma UARTy s různými přenosovými rychlostmi (420k vs. 400k baud)? Docházelo k ztrátě dat nebo synchronizačním chybám?

## 5. Navrhovaná klasifikace

Projekt Adama Mikuliče je technicky výjimečný. Realizoval plně funkční komunikační modul pro letoun s vlastním PCB designem, embedded firmwarem a terénně ověřeným zlepšením dosahu. Jde o práci, která přesahuje gymnaziální rámec a výrazně se přibližuje úrovni bakalářských projektů na technických školách.

**Navrhuji klasifikaci: 1 – výborný**

*Navrhovaná klasifikace bude finálně potvrzena po obhajobě práce před zkušební maturitní komisí.*

---

*Mgr. Aleš Novák, oponent maturitní práce*
*5. 5. 2026*
