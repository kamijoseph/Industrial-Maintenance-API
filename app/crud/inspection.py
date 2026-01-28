
from sqlalchemy.orm import Session
from app.models.inspection import InspectionLog
from app.schemas.inspection import InspectionCreate


def create_inspection(db: Session, data: InspectionCreate) -> InspectionLog:
    inspection = InspectionLog(**data.model_dump())
    db.add(inspection)
    db.commit()
    db.refresh(inspection)
    return inspection


def get_inspection(db: Session, inspection_id: int) -> InspectionLog | None:
    return db.get(InspectionLog, inspection_id)


def list_inspections(db: Session) -> list[InspectionLog]:
    return db.query(InspectionLog).all()
