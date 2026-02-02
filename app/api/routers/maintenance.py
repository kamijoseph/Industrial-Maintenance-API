from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.maintenance import MaintenanceCreate, MaintenanceRead
from app.crud import maintenance as crud

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])


@router.post("/", response_model=MaintenanceRead)
def create_maintenance(payload: MaintenanceCreate, db: Session = Depends(get_db)):
    return crud.create_maintenance(db, payload)


@router.get("/{maintenance_id}", response_model=MaintenanceRead)
def read_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    maintenance = crud.get_maintenance(db, maintenance_id)
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return maintenance


@router.get("/", response_model=list[MaintenanceRead])
def list_maintenance(db: Session = Depends(get_db)):
    return crud.list_maintenance(db)