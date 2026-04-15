import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cohort.json"

app = FastAPI(title="Berkeley Xcelerator Cohort")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "app" / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "app" / "templates"))


def load_cohort():
    with open(DATA_PATH) as f:
        data = json.load(f)
    # Only show featured companies (others are still being collected)
    data["companies"] = [c for c in data["companies"] if c.get("featured")]
    return data


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/yc-style", response_class=HTMLResponse)
def yc_style(request: Request):
    data = load_cohort()
    cats = sorted({c for company in data["companies"] for c in company["categories"]})
    return templates.TemplateResponse(
        request, "yc_style.html", {"cohort": data, "categories": cats}
    )


@app.get("/a16z-style", response_class=HTMLResponse)
def a16z_style(request: Request):
    data = load_cohort()
    return templates.TemplateResponse(request, "a16z_style.html", {"cohort": data})


@app.get("/healthz")
def healthz():
    return {"ok": True}
