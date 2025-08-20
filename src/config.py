from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_env(dotenv_path: Optional[Path] = None) -> None:
    if dotenv_path is None:
        dotenv_path = _PROJECT_ROOT / ".env"
    load_dotenv(dotenv_path)

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

if __name__ == "__main__":
    load_env()
    print("API_KEY:", get_key("API_KEY"))
    print("DATA_DIR:", get_key("DATA_DIR"))
