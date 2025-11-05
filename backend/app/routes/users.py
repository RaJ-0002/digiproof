from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.crud.user import UserCRUD  # Assumes async CRUD class exists

router = APIRouter(prefix="/users", tags=["Users"])

# Initialize the UserCRUD class
user_crud = UserCRUD()

@router.post("/", response_model=User)
async def create_user_endpoint(
    user: UserCreate, db: AsyncSession = Depends(get_session)
):
    try:
        created_user = await user_crud.create(db, user)
        return created_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await user_crud.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
async def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_session),
):
    updated_user = await user_crud.update(db, user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}")
async def delete_user_endpoint(user_id: int, db: AsyncSession = Depends(get_session)):
    success = await user_crud.delete(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
