import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PDD_DOC_PATH = os.getenv("PDD_DOC_PATH", str(Path(__file__).resolve().parent.parent / "pdd_document.txt"))
AI_MODE = os.getenv("AI_MODE", "local")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is required in environment variables")
