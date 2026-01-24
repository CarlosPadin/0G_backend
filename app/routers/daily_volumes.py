from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import MarketDailyVolume
from app.db.session import get_db
from app.schemas.market_volumes import DailyVolume

router = APIRouter()

@router.get(
    "/market-volume/last-7-days",
    response_model=list[DailyVolume]
)
async def get_last_7_days_volume(
    session: AsyncSession = Depends(get_db)
):
    try:
        result = await session.execute(
            select(MarketDailyVolume)
            .order_by(MarketDailyVolume.timestamp.desc())
            .limit(7)
        )

        data = result.scalars().all()

        if not data:
            raise HTTPException(
                status_code=404,
                detail="No market volume data yet"
            )

        return data

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To add values in the daily-volumes table
# @router.post("/market-volume") 
# async def run_daily_volume(background_tasks: BackgroundTasks):
#     background_tasks.add_task(calculate_daily_market_volume)
#     return {"status": "triggered"}