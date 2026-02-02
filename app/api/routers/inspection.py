from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.inspection import InspectionCreate, InspectionRead
from app.crud import inspection as crud

router = APIRouter(prefix="/inspections", tags=["Inspections"])


@router.post("/", response_model=InspectionRead)
def create_inspection(payload: InspectionCreate, db: Session = Depends(get_db)):
    return crud.create_inspection(db, payload)


@router.get("/{inspection_id}", response_model=InspectionRead)
def read_inspection(inspection_id: int, db: Session = Depends(get_db)):
    inspection = crud.get_inspection(db, inspection_id)
    if not inspection:
        raise HTTPException(status_code=404, detail="Inspection not found")
    return inspection


@router.get("/", response_model=list[InspectionRead])
def list_inspections(db: Session = Depends(get_db)):
    return crud.list_inspections(db)