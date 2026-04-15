# Berkeley Xcelerator Cohort Mockup

Internal mockup for the Berkeley Xcelerator cohort page. Two layout options to compare.

## Routes

- `/` — Picker landing
- `/yc-style` — YC directory style: dense filterable grid, search, category chips, expandable cards
- `/a16z-style` — a16z portfolio style: editorial flip cards, hover for founders
- `/healthz` — Health check

## Local dev

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000

## Editing cohort data

All company info lives in `data/cohort.json`. Edit and redeploy — no code changes needed.

## Deploy

Railway picks up `railway.json` and `Procfile`. Push to `main`, Railway builds and deploys.
