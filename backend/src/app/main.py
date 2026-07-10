from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.lifespan import lifespan

app: FastAPI = FastAPI(
    title="Heartbeat",
    description="FastAPI application for the AI Copilot for doctors project.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
