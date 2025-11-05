from typing import List, Optional

from sqlmodel import select, func
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserCRUD:
    async def create(self, db: AsyncSession, user: UserCreate) -> User:
        db_user = User(**user.dict())
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

    async def get(self, db: AsyncSession, user_id: int) -> Optional[User]:
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, db: AsyncSession) -> List[User]:
        result = await db.execute(select(User))
        return result.scalars().all()

    async def get_by_skills(self, db: AsyncSession, skills: List[str]) -> List[User]:
        # Assumes `skills` is a JSONB column (for PostgreSQL)
        result = await db.execute(
            select(User).where(
                func.jsonb_contains(User.skills, skills)
            )
        )
        return result.scalars().all()

    async def update(
        self,
        db: AsyncSession,
        user_id: int,
        user: UserUpdate
    ) -> Optional[User]:
        db_user = await self.get(db, user_id)
        if not db_user:
            return None

        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)

        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

    async def delete(self, db: AsyncSession, user_id: int) -> bool:
        db_user = await self.get(db, user_id)
        if not db_user:
            return False

        await db.delete(db_user)
        await db.commit()
        return True

user_crud = UserCRUD()
