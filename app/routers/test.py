from fastapi import APIRouter
from app.services.fetch_store import fetch_and_store_market_metrics

router = APIRouter()

@router.get("/test-fetch")
async def test_fetch():
    result = await fetch_and_store_market_metrics()
    return {"status": "ok", "result": result}
