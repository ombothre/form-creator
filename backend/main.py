from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from helpers import generate_form, wrap_with_html

app = FastAPI()

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs", status_code=307)

@app.get("/api/generate-form/html", response_class=HTMLResponse)
def get_form():
    try:
        form_html = generate_form()
        full_html = wrap_with_html(form_html)
        return full_html
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
