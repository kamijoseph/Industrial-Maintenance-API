
# equipment routers
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.equipment import EquipmentCreate, EquipmentRead
from app.crud import equipment as crud

router = APIRouter(
    prefix = "/equipment",
    tags = ["Equipment"]
)

@router.post("/", response_model=EquipmentRead)
def create_equipment(
    payload: EquipmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_equipment(db, payload)