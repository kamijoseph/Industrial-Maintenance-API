
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.db.base import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(255),
        nullable = False,
        index = True
    )
    location: Mapped[str] = mapped_column(
        String(255),
        nullable = False
    )
    installed_at: Mapped[datetime] = mapped_column(
        DateTime,
        default = datetime.utcnow
    )

    inspections = relationship(
        "InspectionLog",
        back_populates = "equipment"
    )
    maintenance_schedule = relationship(
        "MaintenanceSchedule",
        back_populates = "equipment"
    )