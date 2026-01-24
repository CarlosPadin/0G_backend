from dotenv import load_dotenv
import os
from typing import Final


load_dotenv()

# COINCAP API
COINCAP_API_KEY = os.getenv("COINCAP_API_KEY")
COINCAP_BASE_URL = os.getenv("COINCAP_BASE_URL")
COINCAP_ASSET_ID = os.getenv("COINCAP_ASSET_ID")

# DATABASE
DATABASE_URL: Final[str] = os.environ["DATABASE_URL"]

# FRONTEND URLs
raw_origins = os.getenv("ORIGINS_URL", "")

ORIGINS_URL: Final[list[str]] = [
    origin.rstrip("/")
    for origin in raw_origins.split(",")
    if origin.strip()
]
