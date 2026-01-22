# from fastapi import APIRouter, Depends
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db

# router = APIRouter()

# @router.get("/health")
# async def health(session: AsyncSession = Depends(get_db)):
#     try:
#         await session.execute(select(1))
#         return {"status": "ok"}
#     except Exception as e:
#         return {"status": "error", "detail": str(e)}

from fastapi import APIRouter
import asyncpg

router = APIRouter()

@router.get("/test-direct")
async def test_direct():
    try:
        # Conexión directa con todos los parámetros correctos
        conn = await asyncpg.connect(
            host='db.udbsyqzicflvjnpdzcew.supabase.co',
            port=6543,
            user='postgres',
            password='76ADkrRzS7qFJwq4',
            database='postgres',
            ssl='require'  # asyncpg usa 'ssl', no 'sslmode'
        )
        
        # Prueba simple
        result = await conn.fetchval('SELECT 1')
        await conn.close()
        
        return {"status": "ok", "result": result}
    except Exception as e:
        return {"status": "error", "detail": str(e)}