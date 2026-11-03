from fastapi import FastAPI

from app.core.config import settings
from app.api.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend for an AI-powered Vedic Astrology application",
    debug=settings.DEBUG
)


app.include_router(
    health_router,
    tags=["Health"]
)


@app.get("/")
async def root():

    return {
        "message": "Welcome to AI Astrology Backend",
        "status": "running",
        "docs": "/docs",
        "health": "/health"
    }