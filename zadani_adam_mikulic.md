# Zadání maturitní práce – Adam Mikulič

## 1. NÁZEV PROJEKTU

Komunikační relay node pro VTOL UAV

---

## 2. CÍL PRÁCE

Vyvinout a otestovat komunikační modul („relay node") rozšiřující dosah UAV a umožňující autonomní let na větší vzdálenosti.

---

## 3. FUNKČNÍ POŽADAVKY

- Návrh a výroba vlastního PCB
- Firmware pro komunikaci a řízení (telemetrie, relay funkce)
- Napájení a energetická optimalizace
- Testování stabilní komunikace na vzdálenost (minimálně 2x rozšíření dosahu)
- Integrace s letounem (držák + bezpečné vypuštění)
- Validace na reálných letových testech

---

## 4. POVINNÉ VÝSTUPY

### 4.1 Funkční projekt

- Funkční relay node včetně PCB
- Firmware s dokumentací
- Úspěšné letové testy

### 4.2 Vědecký/odborný článek

- **Rozsah:** 8-15 stran A4, formát dvou sloupců
- **Obsah:** Analýza komunikačních systémů, návrh řešení, implementace HW/SW, testování
- **Styl:** Mírně populárně-vědecký

### 4.3 Poster

- **Velikost:** A3 (297 × 420 mm)
- **Obsah:** Schéma zapojení, fotografie PCB, výsledky testů komunikace
- **Formát:** PDF pro tisk

### 4.4 Technická dokumentace

- **Rozsah:** Minimálně 10-20 stran
- **Formát:** Markdown nebo PDF (Word/LaTeX)
- **Obsah:** Technické specifikace komponent, schémata zapojení PCB, dokumentace firmware, montážní návod, provozní návod a údržba, testovací protokoly

### 4.5 Prezentace pro obhajobu

- **Rozsah:** 15-20 slidů
- **Trvání:** 10-15 minut + diskuse
- **Obsah:** Video z letových testů, demonstrace komunikace

### 4.6 Výkaz činnosti

- Průběžné reporty (R1, R2, R3)
- Měsíční záznamy o práci včetně odhadovaných hodin

---

## 5. HODNOTICÍ KRITÉRIA

- **Funkčnost projektu (40%)** – Funkční relay node, úspěšné testy
- **Dokumentace (25%)** – Technická dokumentace, článek, poster
- **Prezentace a obhajoba (25%)** – Kvalita prezentace, odpovědi na dotazy
- **Výkaz činnosti (10%)** – Pravidelná práce, dokumentace postupu

---

## 6. STRUKTURA ODEVZDÁNÍ

```tree
/projekt_mikulic/
  ├── README.md (stručný přehled projektu)
  ├── paper.pdf (vědecký článek)
  ├── poster.pdf (poster A3)
  ├── vykaz_cinnosti.xlsx (výkaz průběžné činnosti)
  ├── dokumentace/
  │   └── technicka_dokumentace.pdf nebo .md
  ├── prezentace/
  │   └── obhajoba.pptx
  └── projekt/
      ├── firmware/ (zdrojové kódy)
      ├── hardware/ (schémata PCB, gerber files)
      └── testy/ (protokoly, videa)
```
