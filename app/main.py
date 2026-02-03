from fastapi import FastAPI

# import the routers
from app.api.routers import (
    equipment,
    technician,
    inspection,
    maintenance
)

# initializse app
app = FastAPI(
    title = "Industrial Maintenance API",
    version = "1.0.0",
)

# riuters
app.include_router(equipment.router)
app.include_router(technician.router)
app.include_router(inspection.router)
app.include_router(maintenance.router)