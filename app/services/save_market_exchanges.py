from datetime import datetime, timezone
from app.db.models import MarketExchanges
from app.services.get_market_details import get_market_details 
from app.db.session import async_session

async def save_market_exchanges():
    markets = await get_market_details(limit=20)  # limit set to 20 for testing
    timestamp = datetime.now(timezone.utc)

    async with async_session() as session:
    # Save data in the database
        for item in markets:
            session.add(
                MarketExchanges(
                    exchange_id=item["exchangeId"],
                    base_id=item["baseId"],
                    quote_id=item["quoteId"],
                    base_symbol=item["baseSymbol"],
                    quote_symbol=item["quoteSymbol"],
                    price_usd=float(item["priceUsd"]),
                    volume_usd_24h=float(item["volumeUsd24Hr"]),
                    volume_percent=float(item["volumePercent"]),
                    timestamp=timestamp,
                )
            )

        await session.commit()
