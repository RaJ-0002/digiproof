from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import AsyncSession
from app.db.session import get_session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.crud.project import ProjectCRUD  # Assuming you have a ProjectCRUD class for async methods

router = APIRouter(prefix="/projects", tags=["Projects"])

# Initialize the ProjectCRUD class
project_crud = ProjectCRUD()

@router.post("/", response_model=Project)
async def create_project_endpoint(
    project: ProjectCreate, 
    db: AsyncSession = Depends(get_session)
):
    try:
        return await project_crud.create(db, project)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[Project])
async def read_projects(
    skip: int = 0, 
    limit: int = 100, 
    db: AsyncSession = Depends(get_session)
):
    return await project_crud.get_all(db, skip=skip, limit=limit)

@router.get("/{project_id}", response_model=Project)
async def read_project(
    project_id: int, 
    db: AsyncSession = Depends(get_session)
):
    project = await project_crud.get(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=Project)
async def update_project_endpoint(
    project_id: int,
    project_data: ProjectUpdate,
    db: AsyncSession = Depends(get_session)
):
    updated_project = await project_crud.update(db, project_id, project_data)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

@router.delete("/{project_id}")
async def delete_project_endpoint(
    project_id: int, 
    db: AsyncSession = Depends(get_session)
):
    success = await project_crud.delete(db, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}
