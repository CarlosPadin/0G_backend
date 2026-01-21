from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import ORIGINS_URL
from app.core.scheduler import start_scheduler, shutdown_scheduler
from app.routers import  market_overview, market_exchanges, daily_volumes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    start_scheduler()
    yield
    # SHUTDOWN
    shutdown_scheduler()

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(market_overview.router)
app.include_router(market_exchanges.router)
app.include_router(daily_volumes.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS_URL,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
