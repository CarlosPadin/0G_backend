# from datetime import datetime, timezone
# from sqlalchemy import select

# from app.services.get_market_details import get_market_details
# from app.services.metrics import calculate_metrics
# from app.services.price_change import calculate_price_change
# from app.db.session import async_session
# from app.db.models import MarketMetric

# async def save_market_overview():
#     markets = await get_market_details(limit=20)  # limit set to 20 for testing
#     metrics = calculate_metrics(markets)

#     async with async_session() as session:
#         result = await session.execute(
#             select(MarketMetric)
#             .order_by(MarketMetric.timestamp.desc())
#             .limit(1)
#         )
#         last_metric = result.scalar_one_or_none()

#         price_change = calculate_price_change(
#             metrics["average_price_usd"],
#             last_metric.avg_price_usd if last_metric else None
#         )

#         metric = MarketMetric(
#             asset_id="zero-gravity",
#             timestamp=datetime.now(timezone.utc),
#             avg_price_usd=metrics["average_price_usd"],
#             total_volume_24h=metrics["total_volume_24h"],
#             price_change=price_change
#         )

#         session.add(metric)
#         await session.commit()
