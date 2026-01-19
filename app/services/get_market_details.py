import httpx
from fastapi import HTTPException
from app.core.config import (
    COINCAP_API_KEY,
    COINCAP_BASE_URL,
    COINCAP_ASSET_ID
)

async def get_market_details(limit: int = 20):
    url = f"{COINCAP_BASE_URL}/assets/{COINCAP_ASSET_ID}/markets?limit={limit}"

    headers = {
        "Authorization": f"Bearer {COINCAP_API_KEY}",
        "Accept": "application/json",
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    return response.json()["data"]
