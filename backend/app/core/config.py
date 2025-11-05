from pydantic import BaseSettings, Field, PostgresDsn, validator
from typing import Optional, List, Union


class Settings(BaseSettings):
    # General settings
    PROJECT_NAME: str = "DigiProof"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = Field(default=False, description="Enable debug mode")

    # Database settings
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = Field(default="localhost", env="POSTGRES_SERVER")
    POSTGRES_PORT: str = Field(default="5432", env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    DATABASE_URL: Optional[Union[str, PostgresDsn]] = None

    # JWT Auth settings
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = Field(default=["*"], env="BACKEND_CORS_ORIGINS")

    # AI/ML settings
    AI_MODEL_PATH: Optional[str] = Field(default="./app/ai/model.pkl", env="AI_MODEL_PATH")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @validator("DATABASE_URL", pre=True, always=True)
    def assemble_db_connection(cls, v, values) -> str:
        if isinstance(v, str) and v:
            return v
        return (
            f"postgresql+asyncpg://{values.get('POSTGRES_USER')}:{values.get('POSTGRES_PASSWORD')}"
            f"@{values.get('POSTGRES_SERVER')}:{values.get('POSTGRES_PORT')}/{values.get('POSTGRES_DB')}"
        )


# Instantiate settings globally
settings = Settings()
