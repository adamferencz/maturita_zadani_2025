# Josef Holeček — Webový portál pro kroužky a trenéry v Havlíčkově Brodě

Maturitní práce, Gymnázium Havlíčkův Brod, školní rok 2025/2026.

**Nasazená aplikace:** [krouzky-hb.vercel.app](https://krouzky-hb.vercel.app)

---

## Co je kde

| Složka / soubor | Obsah |
| --- | --- |
| `paper/` | Maturitní článek (PDF + přepis MD) |
| `poster/` | Plakát A3 (PDF) |
| `prezentace/` | Prezentace pro obhajobu (PDF) |
| `dokumentace/` | Technická dokumentace (MD) |
| `projekt/krouzky-hb.zip` | Kompletní zdrojové kódy aplikace |

## Jak spustit projekt

1. Rozbalit `projekt/krouzky-hb.zip`
2. Nainstalovat závislosti: `npm install`
3. Vyplnit Firebase konfiguraci dle `FIREBASE_SETUP.md`
4. Spustit vývojový server: `npm run dev`

Detailní instrukce jsou v `dokumentace/TECHNICKA_DOKUMENTACE.md` a v souborech `projekt/FIREBASE_SETUP.md` a `projekt/ADMIN_SETUP_INSTRUCTIONS.md`.

## Tech stack

- **Frontend:** Next.js 14, React, TypeScript, Tailwind CSS, shadcn/ui
- **Backend / databáze:** Firebase Firestore (real-time), Firebase Auth
- **Nasazení:** Vercel
