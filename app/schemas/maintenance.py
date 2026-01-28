
from pydantic import BaseModel
from datetime import datetime


class MaintenanceBase(BaseModel):
    equipment_id: int
    description: str
    scheduled_for: datetime


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceRead(MaintenanceBase):
    id: int

    model_config = {"from_attributes": True}
