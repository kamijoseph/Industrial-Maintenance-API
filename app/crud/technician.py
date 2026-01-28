
from sqlalchemy.orm import Session
from app.models.technician import Technician
from app.schemas.technician import TechnicianCreate


def create_technician(db: Session, data: TechnicianCreate) -> Technician:
    technician = Technician(**data.model_dump())
    db.add(technician)
    db.commit()
    db.refresh(technician)
    return technician


def get_technician(db: Session, technician_id: int) -> Technician | None:
    return db.get(Technician, technician_id)


def list_technicians(db: Session) -> list[Technician]:
    return db.query(Technician).all()
