from sqlmodel import SQLModel

class BaseModel(SQLModel):
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            list: lambda v: v  # Ensures lists are properly encoded as JSON
        }
        orm_mode = True  # Important for working with ORMs and FastAPI responses
