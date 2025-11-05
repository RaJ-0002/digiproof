from typing import List, Optional
from sqlmodel import Field, SQLModel
from pydantic import validator
from sqlalchemy import JSON  # Import JSON for PostgreSQL
from .base import BaseModel

class User(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=2, max_length=50)
    age: int = Field(gt=13, lt=100, description="Must be between 14-99")
    skills: List[str] = Field(
        default_factory=list,
        sa_type=JSON,  # For PostgreSQL JSONB
        description="List of technical skills",
        min_items=1
    )

    # Optional: Validation example (SQLModel 0.0.8+)
    @validator('skills', each_item=True)
    def validate_skills(cls, value):
        if len(value.strip()) < 2:
            raise ValueError("Skill must be at least 2 characters")
        return value.title()
