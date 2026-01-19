from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.fetch_store import fetch_and_store_market_metrics

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(
        fetch_and_store_market_metrics,
        "interval",
        hours=1   # "hours" "minutes" "seconds" 
    )
    scheduler.start()

def shutdown_scheduler():
    scheduler.shutdown()