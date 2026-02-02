
# equipment routers
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.equipment import EquipmnentCreate
from app.crud import equipment as crud

router = APIRouter(
    prefix = "/equipment",
    tags = ["Equipment"]
)