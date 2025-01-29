from pydantic import BaseModel, Field


class UserBase(BaseModel):
    first_name: str = Field(..., description='Имя')
    last_name: str = Field(..., description='Фамилия')
    middle_name: str | None = Field(..., description='Отчество')

    class Config:
        from_attributes = True


class UserGet(UserBase):
    id: int = Field(...)
    username: str = Field(...)


class UserCreate(UserBase):
    username: str = Field(...)
    password: str = Field(...)


class UserUpdate(BaseModel):
    id: int = Field(...)
    first_name: str | None = Field(..., description='Имя')
    last_name: str | None = Field(..., description='Фамилия')
    middle_name: str | None = Field(..., description='Отчество')
    username: str | None = Field(...)
    password: str | None = Field(...)

    class Config:
        from_attributes = True


class UserDelete(BaseModel):
    id: int = Field(...)
