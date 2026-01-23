# scripts/create_tables.py
import asyncio
import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import engine
# Importar todos los modelos para que estén registrados en Base.metadata
from app.db.models import Base

async def create_all_tables():
    print("=" * 60)
    print("CREANDO TABLAS EN LA BASE DE DATOS")
    print("=" * 60)
    
    print(f"URL de base de datos: {engine.url}")
    print("\nTablas a crear:")
    
    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")
    
    print("\nCreando tablas...")
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ ¡Todas las tablas creadas exitosamente!")
        
        # Verificar qué tablas existen ahora
        from sqlalchemy import text
        async with engine.connect() as conn:
            result = await conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """))
            tables = result.fetchall()
            
            print("\n📊 Tablas en la base de datos después de la creación:")
            for table in tables:
                print(f"  - {table[0]}")
                
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        raise
    
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(create_all_tables())