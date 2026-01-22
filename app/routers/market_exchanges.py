from fastapi import APIRouter, HTTPException
from sqlalchemy import select
# from app.db.session import async_session
from app.db.models import MarketExchanges
from app.schemas.market_exchanges import MarketExchanges as MarketExchangeSchema 

router = APIRouter()

# @router.get("/exchanges/latest", response_model=list[MarketExchangeSchema])
# async def get_latest_market_snapshot():
#     async with async_session() as session:
#         # Search for the last timestamp
#         result = await session.execute(
#             select(MarketExchanges.timestamp)
#             .order_by(MarketExchanges.timestamp.desc())
#             .limit(1)
#         )
#         last_timestamp = result.scalar_one_or_none()

#         if not last_timestamp:
#             raise HTTPException(status_code=404, detail="No market snapshots yet")

#         # Search for snapshots with the same timestamp
#         result = await session.execute(
#             select(MarketExchanges)
#             .where(MarketExchanges.timestamp == last_timestamp)
#         )
#         data = result.scalars().all()

#     return [MarketExchangeSchema.model_validate(val) for val in data]
