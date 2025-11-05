from typing import List, Optional

from sqlmodel import select, func
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

class ProjectCRUD:
    async def create(self, db: AsyncSession, project: ProjectCreate) -> Project:
        db_project = Project(**project.dict())
        db.add(db_project)
        await db.commit()
        await db.refresh(db_project)
        return db_project

    async def get(self, db: AsyncSession, project_id: int) -> Optional[Project]:
        result = await db.execute(
            select(Project).where(Project.id == project_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, db: AsyncSession) -> List[Project]:
        result = await db.execute(select(Project))
        return result.scalars().all()

    async def get_by_requirements(
        self,
        db: AsyncSession,
        skills: List[str]
    ) -> List[Project]:
        # Assumes `required_skills` is stored as a JSON array
        result = await db.execute(
            select(Project).where(
                func.jsonb_contains(Project.required_skills, skills)  # works only with PostgreSQL
            )
        )
        return result.scalars().all()

    async def update(
        self,
        db: AsyncSession,
        project_id: int,
        project: ProjectUpdate
    ) -> Optional[Project]:
        db_project = await self.get(db, project_id)
        if not db_project:
            return None

        project_data = project.dict(exclude_unset=True)
        for key, value in project_data.items():
            setattr(db_project, key, value)

        db.add(db_project)
        await db.commit()
        await db.refresh(db_project)
        return db_project

    async def delete(self, db: AsyncSession, project_id: int) -> bool:
        db_project = await self.get(db, project_id)
        if not db_project:
            return False

        await db.delete(db_project)
        await db.commit()
        return True

project_crud = ProjectCRUD()
