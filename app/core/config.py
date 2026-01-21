from dotenv import load_dotenv
import os

load_dotenv()

COINCAP_API_KEY = os.getenv("COINCAP_API_KEY")
COINCAP_BASE_URL = os.getenv("COINCAP_BASE_URL")
COINCAP_ASSET_ID = os.getenv("COINCAP_ASSET_ID")

# Convert ORIGINS_URL to list
ORIGINS_URL = os.getenv("ORIGINS_URL", "")
ORIGINS_URL = [origin.strip() for origin in ORIGINS_URL.split(",") if origin.strip()]
