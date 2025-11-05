from typing import AsyncGenerator
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# --- Create Async Engine ---
engine = create_async_engine(
    settings.DATABASE_URL,  # already assembled by pydantic validator
    echo=settings.DEBUG,
    future=True
    # ❌ Remove pool_size and max_overflow: not supported for async engines
)

# --- Async Session Factory ---
async_session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# --- Dependency to Get DB Session ---
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

# --- Initialize the DB (Create Tables) ---
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
