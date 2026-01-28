
# equipment crud
from sqlalchemy.orm import Session
from app.models.equipment import Equipment
from app.schemas.equipment import EquipmnentCreate

def create_equipment(db: Session, data: EquipmnentCreate) -> Equipment:
    equipment = Equipment(**data.model_dump())
    db.add(equipment)
    db.commit()
    db.refresh(equipment)
    return equipment

def get_equipment(db: Session, equipment_id: int) -> Equipment | None:
    return db.get(Equipment, equipment_id)

def list_equipment(db: Session) -> list[Equipment]:
    return db.query(Equipment).all()