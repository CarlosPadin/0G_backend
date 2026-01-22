from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_size=5,
    max_overflow=10
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# Dependency
async def get_db():
    async with async_session() as session:
        yield session
