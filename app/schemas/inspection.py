
from pydantic import BaseModel
from datetime import datetime


class InspectionBase(BaseModel):
    equipment_id: int
    technician_id: int
    notes: str | None = None


class InspectionCreate(InspectionBase):
    pass


class InspectionRead(InspectionBase):
    id: int
    inspected_at: datetime

    model_config = {"from_attributes": True}
