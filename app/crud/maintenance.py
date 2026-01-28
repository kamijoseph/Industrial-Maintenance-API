
from sqlalchemy.orm import Session
from app.models.maintenance import MaintenanceSchedule
from app.schemas.maintenance import MaintenanceCreate


def create_maintenance(db: Session, data: MaintenanceCreate) -> MaintenanceSchedule:
    maintenance = MaintenanceSchedule(**data.model_dump())
    db.add(maintenance)
    db.commit()
    db.refresh(maintenance)
    return maintenance


def get_maintenance(db: Session, maintenance_id: int) -> MaintenanceSchedule | None:
    return db.get(MaintenanceSchedule, maintenance_id)


def list_maintenance(db: Session) -> list[MaintenanceSchedule]:
    return db.query(MaintenanceSchedule).all()
