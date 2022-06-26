import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "db.sqlite"
UPLOAD_DIR = BASE_DIR / "uploads"


def get_database_path():
    return str(DATABASE_PATH)


def get_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    return str(UPLOAD_DIR)
