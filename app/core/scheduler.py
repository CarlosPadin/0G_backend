from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from app.services.save_market_overview import save_market_overview
# from app.services.save_market_exchanges import save_market_exchanges
# from app.services.save_market_volumes import calculate_daily_market_volume

scheduler = AsyncIOScheduler()
interval = 30  # for testing

def start_scheduler():
    # save market metrics overview
    # scheduler.add_job(
    #     save_market_overview,
    #     "interval",
    #     minutes=interval   # "minutes" "minutes" "seconds" 
    # )

    # # save market exchanges
    # scheduler.add_job(
    #     save_market_exchanges,
    #     "interval",
    #     minutes=interval  
    # )

    # # calculate daily market volume
    # scheduler.add_job(
    #     calculate_daily_market_volume,
    #     "cron",
    #     hour=0, # every day at midnight
    #     minute=1,
    # )
    scheduler.start()

def shutdown_scheduler():
    scheduler.shutdown()