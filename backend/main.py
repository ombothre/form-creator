from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import logging
from helpers import generate_form, wrap_with_html

# Set up logging
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.INFO,  # Logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)
logger = logging.getLogger(__name__)

app = FastAPI()

os.makedirs("generated", exist_ok=True)

@app.get("/generate-form", response_class=HTMLResponse)
def get_form():
    try:
        logger.info("Generating form...")
        form_html = generate_form()
        full_html = wrap_with_html(form_html)
        with open("generated/form.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        logger.info("Form generated successfully.")
        return full_html
    except Exception as e:
        logger.error(f"Error generating form: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An error occurred while generating the form.")

app.mount("/generated", StaticFiles(directory="generated"), name="generated")
