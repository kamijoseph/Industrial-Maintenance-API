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

app.include_router(equipment.router)
app.include_router(technician.router)
app.include_router(inspection.router)
app.include_router(maintenance.router)