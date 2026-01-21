from datetime import datetime, timezone
from sqlalchemy import select, desc

from app.db.models import MarketExchanges
from app.services.get_market_details import get_market_details
from app.db.session import async_session

async def save_market_exchanges():
    markets = await get_market_details(limit=20)
    timestamp = datetime.now(timezone.utc)

    async with async_session() as session:
        for item in markets:
            current_price = float(item["priceUsd"])

            result = await session.execute(
                select(MarketExchanges)
                .where(
                    MarketExchanges.exchange_id == item["exchangeId"],
                    MarketExchanges.base_id == item["baseId"],
                    MarketExchanges.quote_id == item["quoteId"],
                )
                .order_by(desc(MarketExchanges.timestamp))
                .limit(1)
            )

            last_record = result.scalar_one_or_none()

            # Price change calculation
            price_change = (
                current_price - last_record.price_usd
                if last_record
                else None
            )

            session.add(
                MarketExchanges(
                    exchange_id=item["exchangeId"],
                    base_id=item["baseId"],
                    quote_id=item["quoteId"],
                    base_symbol=item["baseSymbol"],
                    quote_symbol=item["quoteSymbol"],
                    price_usd=current_price,
                    volume_usd_24h=float(item["volumeUsd24Hr"]),
                    volume_percent=float(item["volumePercent"]),
                    price_change=price_change,
                    timestamp=timestamp,
                )
            )

        await session.commit()

