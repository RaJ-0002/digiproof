from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import async_session_factory

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides an async SQLAlchemy session.
    """
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
