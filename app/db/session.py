# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from app.core.config import DATABASE_URL

# engine = create_async_engine(
#     DATABASE_URL,
#     echo=False,
#     pool_size=10,
#     max_overflow=20
# )

# async_session = async_sessionmaker(
#     engine,
#     expire_on_commit=False
# )

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_size=5,       # reduce un poco para Supabase
    max_overflow=10
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
