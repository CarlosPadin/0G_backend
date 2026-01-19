from dotenv import load_dotenv
import os

load_dotenv()

COINCAP_API_KEY = os.getenv("COINCAP_API_KEY")
COINCAP_BASE_URL = "https://rest.coincap.io/v3"
COINCAP_ASSET_ID = "zero-gravity"
