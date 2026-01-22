from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.cleanup_old_data import cleanup_old_market_data

scheduler = AsyncIOScheduler()

# Every day at 3:00 AM
def start_maintenance_jobs():
    scheduler.add_job(
        cleanup_old_market_data,
        trigger="cron",
        day=1,
        hour=3,
        minute=0,
        id="cleanup_old_market_data",
        replace_existing=True,
    )

    scheduler.start()
