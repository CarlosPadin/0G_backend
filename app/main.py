from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import ORIGINS_URL
from app.core.scheduler import start_scheduler, shutdown_scheduler
from app.db.models import Base
from app.db.session import engine
from app.routers import  market_overview, market_exchanges, daily_volumes
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    start_scheduler()
    yield
    # SHUTDOWN
    shutdown_scheduler()

app = FastAPI(lifespan=lifespan)
app.include_router(market_overview.router)
app.include_router(market_exchanges.router)
app.include_router(daily_volumes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS_URL,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
