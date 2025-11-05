from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.base import init_db, check_db_connection
from app.routes import users, projects, ai

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-Powered Project Matching System",
    version="0.1.0",
    contact={
        "name": "API Support",
        "email": "support@digiproof.com"
    },
    license_info={
        "name": "MIT",
    },
    debug=settings.DEBUG
)

#  CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Routers
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Users"])
app.include_router(projects.router, prefix=f"{settings.API_V1_STR}/projects", tags=["Projects"])
app.include_router(ai.router, prefix=f"{settings.API_V1_STR}/ai", tags=["AI"])

#  Startup Event
@app.on_event("startup")
async def on_startup():
    await init_db()
    if settings.DEBUG:
        print(" Database initialized successfully")

#  Root
@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": f" Welcome to {settings.PROJECT_NAME} API",
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc"
        }
    }

#  Health Check
@app.get("/health", tags=["System"])
async def health_check():
    db_status = await check_db_connection()
    return {
        "status": "healthy",
        "database": "connected" if db_status else "disconnected"
    }
