from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import MarketMetric
from app.db.session import get_db 
from app.schemas.market_metrics import MarketMetric as MarketMetricSchema

router = APIRouter()

@router.get("/overview", response_model=MarketMetricSchema)
async def get_latest_metric(session: AsyncSession = Depends(get_db)):
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))