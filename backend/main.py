from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from helpers import generate_form, wrap_with_html
from datetime import datetime

app = FastAPI()

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs", status_code=307)

@app.get("/api/generate-form/html", response_class=HTMLResponse)
def get_form(request: Request):
    try:
        # Log the IP and time of each request
        print(f"[{datetime.now()}] Generating form for: {request.client.host}")

        form_html = generate_form()

        # Optional: Append timestamp for visual confirmation of freshness
        form_html += f"<p style='text-align:center; font-size:10pt;'>Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"

        full_html = wrap_with_html(form_html)

        return Response(
            content=full_html,
            media_type="text/html",
            headers={
                "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
