from pydantic import BaseModel


class TechnicianBase(BaseModel):
    name: str
    specialization: str


class TechnicianCreate(TechnicianBase):
    pass


class TechnicianRead(TechnicianBase):
    id: int

    model_config = {"from_attributes": True}
