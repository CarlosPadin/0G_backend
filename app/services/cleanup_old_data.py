# app/services/cleanup_old_data.py
from datetime import datetime, timezone, timedelta
from sqlalchemy import delete

from app.db.session import async_session
from app.db.models import (
    MarketDailyVolume,
    MarketMetric,
    MarketExchanges

)

async def cleanup_old_market_data():
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=365)

    async with async_session() as session:
        await session.execute(
            delete(MarketDailyVolume).where(
                MarketDailyVolume.timestamp < cutoff_date
            )
        )

        await session.execute(
            delete(MarketMetric).where(
                MarketMetric.timestamp < cutoff_date
            )
        )

        await session.execute(
            delete(MarketExchanges).where(
                MarketExchanges.timestamp < cutoff_date
            )
        )

        await session.commit()
      
    print(f"Maintenance done, records before {cutoff_date} deleted")
