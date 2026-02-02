from pydantic import BaseModel
from datetime import datetime

class EquipmentBase(BaseModel):
    name: str
    location: str

class EquipmentCreate(EquipmentBase):
    pass

class EquipmentRead(EquipmentBase):
    id: int
    installed_at: datetime

    model_config = {
        "from_attributes": True
    }