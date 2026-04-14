from fastapi import FastAPI

from app.routes.extract import router as extract_router
from app.routes.health import router as health_router


app = FastAPI(title="Reallist Vision Sidecar", version="0.1.0")
app.include_router(health_router, prefix="/api/v1")
app.include_router(extract_router, prefix="/api/v1")
