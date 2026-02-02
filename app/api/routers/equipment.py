
# equipment routers
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.equipment import EquipmentCreate, EquipmentRead
from app.crud import equipment as crud

from typing import List

router = APIRouter(
    prefix = "/equipment",
    tags = ["Equipment"]
)

# create equipment post router
@router.post("/", response_model=EquipmentRead)
def create_equipment(
    payload: EquipmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_equipment(db, payload)

# get equipment router
@router.get("/", response_model=List[EquipmentRead])
def read_equipment(
    equipment_id: int,
    db: Session = Depends(get_db)
):
    equipment = crud.get_equipment(db, equipment_id)
    if not equipment:
        raise HTTPException(
            status_code = 404,
            detail = "Equipment not found"
        )
    return equipment

# list equipments
@router.get("/", response_model=List[EquipmentRead])
def list_equipment(
    db: Session = Depends(get_db)
):
    return crud.list_equipment(db)