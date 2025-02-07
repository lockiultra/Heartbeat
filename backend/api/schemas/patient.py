from backend.api.schemas.user import UserBase, UserGet, UserCreate, UserUpdate, UserDelete
from pydantic import Field


class PatientBase(UserBase):
    insurance: str = Field(...)


class PatientGet(UserGet, PatientBase):
    pass


class PatientCreate(UserCreate, PatientBase):
    pass


class PatientUpdate(UserUpdate):
    insurance: str | None = Field(None)

    class Config:
        from_attributes = True


class PatientDelete(UserDelete):
    pass
