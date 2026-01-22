from fastapi import APIRouter, BackgroundTasks
from sqlalchemy import select

from app.schemas.market_volumes import DailyVolume
# from app.services.save_market_volumes import calculate_daily_market_volume
# from app.db.session import async_session
from app.db.models import MarketDailyVolume

router = APIRouter()

# @router.post("/calculate-daily-volume")     # just for testing
# async def run_daily_volume(background_tasks: BackgroundTasks):
#     background_tasks.add_task(calculate_daily_market_volume)
#     return {"status": "triggered"}


# @router.get("/market-volume/last-7-days", response_model=list[DailyVolume])
# async def get_last_7_days_volume():
#     async with async_session() as session:
#         result = await session.execute(
#             select(MarketDailyVolume)
#             .order_by(MarketDailyVolume.timestamp.desc())
#             .limit(7)
#         )

#         return result.scalars().all()
