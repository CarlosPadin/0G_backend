from datetime import datetime, timezone
from sqlalchemy import select, func, and_
from sqlalchemy.orm import aliased
from app.db.session import async_session
from app.db.models import MarketExchanges, MarketDailyVolume

async def calculate_daily_market_volume():
    midnight_utc = datetime.now(timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    me = aliased(MarketExchanges)

    async with async_session() as session:
        # Last market snapshot
        subquery = (
            select(
                me.exchange_id,
                me.base_id,
                me.quote_id,
                func.max(me.timestamp).label("max_ts"),
            )
            .where(me.timestamp < midnight_utc)
            .group_by(
                me.exchange_id,
                me.base_id,
                me.quote_id,
            )
            .subquery()
        )

        # Sum of market volumes
        result = await session.execute(
            select(func.sum(MarketExchanges.volume_usd_24h))
            .join(
                subquery,
                and_(
                    MarketExchanges.exchange_id == subquery.c.exchange_id,
                    MarketExchanges.base_id == subquery.c.base_id,
                    MarketExchanges.quote_id == subquery.c.quote_id,
                    MarketExchanges.timestamp == subquery.c.max_ts,
                )
            )
        )

        total_volume = result.scalar() or 0.0

        # Save data in the database
        session.add(
            MarketDailyVolume(
                timestamp=midnight_utc,
                volume_usd_24h=total_volume,
            )
        )

        await session.commit()
