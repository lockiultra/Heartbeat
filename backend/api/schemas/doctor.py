from backend.api.schemas.user import *


class DoctorBase(UserBase):
    speciality: str = Field(...)


class DoctorGet(UserGet, DoctorBase):
    pass


class DoctorCreate(UserCreate, DoctorBase):
    pass


class DoctorUpdate(UserUpdate):
    speciality: str | None = Field(None)


class DoctorDelete(UserDelete):
    pass
