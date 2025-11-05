from typing import List, Optional
from pydantic import BaseModel, Field, validator

# Base user schema for shared fields
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=13, lt=100, description="Age must be between 14-99")
    skills: List[str] = Field(..., min_items=1)

    # Method to validate skills
    @validator("skills", each_item=True)
    def validate_skills(cls, skill):
        skill = skill.strip().lower()
        if not skill.replace(" ", "").isalnum():
            raise ValueError("Skills should only contain letters, numbers, and spaces")
        return skill

# Schema for creating a user
class UserCreate(UserBase):
    pass  # Inherits validation and fields from UserBase

# Schema for updating a user
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    age: Optional[int] = Field(None, gt=13, lt=100)
    skills: Optional[List[str]] = Field(None, min_items=1)

    # Validator for skills when present
    @validator("skills", each_item=True)
    def validate_skills(cls, skill):
        if skill:
            skill = skill.strip().lower()
            if not skill.replace(" ", "").isalnum():
                raise ValueError("Skills should only contain letters, numbers, and spaces")
            return skill

# Schema for returning user response
class UserResponse(UserBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "age": 25,
                "skills": ["python", "fastapi"],
                "created_at": "2023-08-15T12:34:56Z"
            }
        }
