from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import SQLAlchemyError
from backend.app.core.config import settings

router = APIRouter(tags=["health"])

@router.get("/health/db")
async def check_db():
    """
    Try to open and immediately close a connection. 
    Returns 204 if OK, 500 if not.
    """
    try:
        engine = create_async_engine(
            settings.DATABASE_URL,
            echo=False,
        )
        # Acquire and release a single connection
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        await engine.dispose()
        return {"status": "ok"}
    except SQLAlchemyError as e:
        # Log e if you want more details
        raise HTTPException(status_code=500, detail="Database connection failed")
