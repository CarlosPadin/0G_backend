from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import MarketExchanges
from app.db.session import get_db
from app.schemas.market_exchanges import MarketExchanges as MarketExchangeSchema

router = APIRouter()

@router.get("/exchanges", response_model=list[MarketExchangeSchema])
async def get_latest_market_snapshot(
    session: AsyncSession = Depends(get_db)
):
    try:
        # Get last timestamp
        result = await session.execute(
            select(MarketExchanges.timestamp)
            .order_by(MarketExchanges.timestamp.desc())
            .limit(1)
        )
        last_timestamp = result.scalar_one_or_none()

        if not last_timestamp:
            raise HTTPException(
                status_code=404,
                detail="No market snapshots yet"
            )

        # Get all snapshots with that timestamp
        result = await session.execute(
            select(MarketExchanges)
            .where(MarketExchanges.timestamp == last_timestamp)
        )
        data = result.scalars().all()

        return [
            MarketExchangeSchema.model_validate(item)
            for item in data
        ]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
