from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.technician import TechnicianCreate, TechnicianRead
from app.crud import technician as crud

router = APIRouter(prefix="/technicians", tags=["Technicians"])


@router.post("/", response_model=TechnicianRead)
def create_technician(payload: TechnicianCreate, db: Session = Depends(get_db)):
    return crud.create_technician(db, payload)


@router.get("/{technician_id}", response_model=TechnicianRead)
def read_technician(technician_id: int, db: Session = Depends(get_db)):
    technician = crud.get_technician(db, technician_id)
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    return technician


@router.get("/", response_model=list[TechnicianRead])
def list_technicians(db: Session = Depends(get_db)):
    return crud.list_technicians(db)