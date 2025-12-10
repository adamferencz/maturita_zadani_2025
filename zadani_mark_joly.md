# Zadání maturitní práce – Mark Joly

## 1. NÁZEV PROJEKTU

VTOL UAV letoun schopný přenášet komunikační modul

---

## 2. CÍL PRÁCE

Sestrojit funkční VTOL letoun schopný vertikálního vzletu, stabilního horizontálního letu a nesení 250 g payloadu (relay node).

---

## 3. FUNKČNÍ POŽADAVKY

- Kompletní CAD návrh konstrukce
- Výroba uhlíkové kostry
- Výroba EPP částí křídla a ocasních ploch
- Tilt-rotor mechanismus pro VTOL
- Integrace autopilota (Pixhawk nebo podobný)
- Letové testy a ladění PID regulátorů
- Validace autonomní waypoint mise
- Payload kapacita minimálně 250 g

---

## 4. POVINNÉ VÝSTUPY

### 4.1 Funkční projekt

- Postavený a funkční VTOL letoun
- Úspěšné letové testy (VTOL + horizontální let)
- Validace mise s payloadem

### 4.2 Vědecký/odborný článek

- **Rozsah:** 8-15 stran A4, formát dvou sloupců
- **Obsah:** Analýza VTOL konceptů, mechanický návrh, výroba, ladění, letové testy
- **Styl:** Mírně populárně-vědecký

### 4.3 Poster

- **Velikost:** A3 (297 × 420 mm)
- **Obsah:** CAD vizualizace, fotografie konstrukce, letové charakteristiky
- **Formát:** PDF pro tisk

### 4.4 Technická dokumentace

- **Rozsah:** Minimálně 10-20 stran
- **Formát:** Markdown nebo PDF (Word/LaTeX)
- **Obsah:** CAD modely a mechanické výkresy, výrobní postup (krok za krokem), montážní návod, nastavení autopilota a PID parametry, provozní návod, fotodokumentace výroby, testovací protokoly a videa z letů

### 4.5 Prezentace pro obhajobu

- **Rozsah:** 15-20 slidů
- **Trvání:** 10-15 minut + diskuse
- **Obsah:** Video z letových testů, demonstrace VTOL přechodu

### 4.6 Výkaz činnosti

- Průběžné reporty (R1, R2, R3)
- Měsíční záznamy o práci včetně odhadovaných hodin

---

## 5. HODNOTICÍ KRITÉRIA

- **Funkčnost projektu (40%)** – Funkční VTOL, úspěšné testy s payloadem
- **Dokumentace (25%)** – Technická dokumentace, článek, poster
- **Prezentace a obhajoba (25%)** – Kvalita prezentace, odpovědi na dotazy
- **Výkaz činnosti (10%)** – Pravidelná práce, dokumentace postupu

---

## 6. STRUKTURA ODEVZDÁNÍ

```tree
/projekt_joly/
  ├── README.md (stručný přehled projektu)
  ├── paper.pdf (vědecký článek)
  ├── poster.pdf (poster A3)
  ├── vykaz_cinnosti.xlsx (výkaz průběžné činnosti)
  ├── dokumentace/
  │   └── technicka_dokumentace.pdf nebo .md
  ├── prezentace/
  │   └── obhajoba.pptx
  └── projekt/
      ├── CAD/ (modely, výkresy)
      ├── konfigurace/ (parametry autopilota)
      ├── fotodokumentace/
      └── videa/ (letové testy)
```
