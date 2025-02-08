from pydantic import BaseModel, Field
from datetime import datetime


class AppointmentGet(BaseModel):
    id: int = Field(...)


class AppointmentCreate(BaseModel):
    name: str = Field(...)
    time: datetime = Field(...)
    doctor_id: int = Field(...)
    patient_id: int = Field(...)

    class Config:
        from_attributes = True


class AppointmentUpdate(BaseModel):
    id: int = Field(...)
    time: datetime | None = Field(None)
    doctor_id: int | None = Field(None)
    patient_id: int | None = Field(None)

    class Config:
        from_attributes = True


class AppointmentDelete(BaseModel):
    id: int = Field(...)
