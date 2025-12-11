# Zadání maturitní práce

**Student:** Mark Joly  
**Školní rok:** 2025/2026  
**Předmět:** Informatika  
**Vedoucí práce:** Ing. Adam Ferencz

## 1. NÁZEV PRÁCE

Bezpilotní letoun s vertikálním vzletem (VTOL) schopný přenášet komunikační modul

---

## 2. CÍL PRÁCE

Sestrojit funkční VTOL letoun schopný vertikálního vzletu, stabilního horizontálního letu a nesení 250 g payloadu (relay node).

---

## 3. FUNKČNÍ POŽADAVKY

- Kompletní 3D návrh konstrukce
- Výroba uhlíkové kostry
- Výroba pěnových částí křídla a ocasních ploch
- Mechanismus naklopení rotorů pro vertikální vzlet
- Integrace autopilota (Pixhawk nebo podobný)
- Letové testy a ladění regulátorů stability letu
- Validace autonomní mise s navigačními body
- Kapacita nákladu minimálně 250 g

---

## 4. POVINNÉ VÝSTUPY

### 4.1 Funkční projekt

- Postavený a funkční VTOL letoun
- Úspěšné letové testy (VTOL + horizontální let)
- Validace mise s payloadem

### 4.2 Vědecký/odborný článek

- **Rozsah:** 8-15 stran A4, formát dvou sloupců
- **Obsah:** Analýza konceptů letounů s vertikálním vzletem, mechanický návrh, výroba, ladění, letové testy
- **Styl:** Mírně populárně-vědecký

### 4.3 Poster

- **Velikost:** A3 (297 × 420 mm)
- **Obsah:** 3D vizualizace, fotografie konstrukce, letové charakteristiky
- **Formát:** PDF pro tisk

### 4.4 Technická dokumentace

- **Rozsah:** Minimálně 10-20 stran
- **Formát:** Markdown nebo PDF (Word/LaTeX)
- **Obsah:** 3D modely a mechanické výkresy, výrobní postup (krok za krokem), montážní návod, nastavení autopilota a parametry regulátorů, provozní návod, fotodokumentace výroby, testovací protokoly a videa z letů

### 4.5 Prezentace pro obhajobu

- **Rozsah:** 5-12 slidů
- **Délka obhajoby:** 15 minut

---

## 5. HODNOTICÍ KRITÉRIA

- **Funkčnost projektu (40%)** – Funkční letoun s vertikálním vzletem, úspěšné testy s nákladem
- **Dokumentace (25%)** – Technická dokumentace, článek, poster
- **Prezentace a obhajoba (35%)** – Kvalita prezentace, odpovědi na dotazy

---

## 6. TERMÍN ODEVZDÁNÍ

**30. dubna 2025**

---

## 7. POSUDKY A HODNOCENÍ

Po odevzdání práce bude vypracován:

- **Posudek vedoucího práce** – hodnocení procesu tvorby, technického řešení a kvality výstupů
- **Posudek oponenta** – nezávislé hodnocení projektu a dokumentace

Na základě obou posudků a obhajoby komise stanoví výsledné hodnocení.

---

## 8. STRUKTURA ODEVZDÁNÍ

Počet vyhotovení: 1x zip soubor s prací a kompletními materiály.

```tree
/projekt_joly/
  ├── README.md (stručný přehled projektu)
  ├── paper.pdf (vědecký článek)
  ├── poster.pdf (poster A3)
  ├── dokumentace/
  │   └── technicka_dokumentace.pdf nebo .md
  ├── prezentace/
  │   └── obhajoba.pptx
  └── projekt/
      ├── 3D_modely/ (modely, výkresy)
      ├── konfigurace/ (parametry autopilota)
      ├── fotodokumentace/
      └── videa/ (letové testy)
```
