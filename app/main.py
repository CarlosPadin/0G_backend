from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.scheduler import start_scheduler, shutdown_scheduler
from app.db.models import Base
from app.db.session import engine
from app.routers import  market_overview, market_exchanges
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

origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
]


app = FastAPI(lifespan=lifespan)
app.include_router(market_overview.router)
app.include_router(market_exchanges.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}
