from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.models import MarketExchanges
from app.schemas.market_exchanges import MarketExchanges as MarketExchangeSchema

router = APIRouter()

@router.get("/health")
async def health(session: AsyncSession = Depends(get_db)):
    try:
        await session.execute(select(1))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
