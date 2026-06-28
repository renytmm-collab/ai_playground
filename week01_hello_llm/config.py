import os
from pathlib import Path


ENV_PATH = Path(__file__).with_name(".env")

try:
    from dotenv import load_dotenv
except ImportError:
    DOTENV_AVAILABLE = False
else:
    DOTENV_AVAILABLE = True
    load_dotenv(ENV_PATH, encoding="utf-8-sig")


API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://api.deepseek.com")
MODEL = os.getenv("MODEL", "deepseek-v4-flash")


def validate_config():
    if ENV_PATH.exists() and not DOTENV_AVAILABLE:
        return "python-dotenv is not installed. Please run: pip install -r requirements.txt"
    if not API_KEY:
        return "API_KEY is missing. Please create .env from .env.example and fill in your DeepSeek API key."
    return None
