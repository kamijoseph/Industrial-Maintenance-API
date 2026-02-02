from fastapi import FastAPI

from app.api.routers import (
    equipment,
    technician,
    inspection,
    maintenance
)

app = FastAPI(
    title = "Industrial Maintenance API",
    version = "1.0.0",
)