from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.db.models import MarketMetric
from app.db.session import async_session
from app.schemas.market_metrics import MarketMetric as MarketMetricSchema

router = APIRouter()

@router.get("/metrics/overview", response_model=MarketMetricSchema)
async def get_latest_metric():
    async with async_session() as session:
        result = await session.execute(
            select(MarketMetric)
            .order_by(MarketMetric.timestamp.desc())
            .limit(1)
        )
        metric = result.scalar_one_or_none()

        if not metric:
          raise HTTPException(
            status_code=404,
            detail="No metrics yet"
          )

    return MarketMetricSchema.model_validate(metric)
