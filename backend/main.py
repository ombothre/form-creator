from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import logging
from helpers import generate_form, wrap_with_html

# Configure logger
logger = logging.getLogger("uvicorn.error")  # Use uvicorn-compatible logger
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

app = FastAPI()

os.makedirs("generated", exist_ok=True)

@app.get("/")
def read_root():
    logger.info("Root endpoint called.")
    return {"message": "API is working!"}

@app.get("/api/generate-form/html", response_class=HTMLResponse)
def get_form():
    try:
        logger.info("Generating form...")
        form_html = generate_form()
        full_html = wrap_with_html(form_html)
        with open("generated/form.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        logger.info("Form generated and saved to generated/form.html")
        return full_html
    except Exception as e:
        logger.exception("Error generating form:")
        raise HTTPException(status_code=500, detail="An error occurred while generating the form.")

# Mount static directory
app.mount("/generated", StaticFiles(directory="generated"), name="generated")
