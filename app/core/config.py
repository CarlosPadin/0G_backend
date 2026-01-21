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
ORIGINS_URL = os.getenv("ORIGINS_URL", "")
ORIGINS_URL = [origin.strip() for origin in ORIGINS_URL.split(",") if origin.strip()]
