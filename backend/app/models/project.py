from typing import List, Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import JSON  # Import JSON for PostgreSQL
from .base import BaseModel

class Project(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=5, max_length=100)
    required_skills: List[str] = Field(
        default_factory=list,
        sa_type=JSON,  # For PostgreSQL JSONB
        description="Skills needed for this project",
        min_items=1
    )
    owner_id: Optional[int] = Field(
        default=None,
        foreign_key="user.id",
        description="Project creator reference"
    )

    # Example method for skill analysis
    def skill_overlap(self, user_skills: List[str]) -> List[str]:
        return list(set(self.required_skills) & set(user_skills))
