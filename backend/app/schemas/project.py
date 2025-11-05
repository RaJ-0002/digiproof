from typing import List, Optional
from pydantic import BaseModel, Field, validator

# Base schema for project fields
class ProjectBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=200)
    required_skills: List[str] = Field(..., min_items=1)

    # Validator to clean and validate skills input
    @validator("required_skills", each_item=True)
    def validate_skills(cls, skill):
        skill = skill.strip().lower()  # Clean skill: strip whitespaces and convert to lowercase
        if not skill.replace(" ", "").isalnum():  # Ensure the skill is alphanumeric
            raise ValueError("Skills should only contain letters, numbers, and spaces")
        return skill

# Schema for creating a project
class ProjectCreate(ProjectBase):
    pass  # Inherits validation and fields from ProjectBase

# Schema for updating a project
class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=200)
    required_skills: Optional[List[str]] = Field(None, min_items=1)

    # Validator to clean and validate skills input (only if present)
    @validator("required_skills", each_item=True)
    def validate_skills(cls, skill):
        if skill:
            skill = skill.strip().lower()  # Clean skill: strip whitespaces and convert to lowercase
            if not skill.replace(" ", "").isalnum():  # Ensure the skill is alphanumeric
                raise ValueError("Skills should only contain letters, numbers, and spaces")
            return skill

# Schema for project response with ID and timestamps
class ProjectResponse(ProjectBase):
    id: int
    created_at: Optional[str] = None  # Assuming this field will be populated by the DB
    updated_at: Optional[str] = None  # Assuming this field will be populated by the DB

    class Config:
        orm_mode = True  # Allow ORM models to be used with Pydantic
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "AI Matching System",
                "required_skills": ["machine learning", "python"],
                "created_at": "2023-08-15T12:34:56Z"
            }
        }
