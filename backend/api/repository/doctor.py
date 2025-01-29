from backend.api.repository.base import BaseRepository
from backend.api.models.doctor import Doctor
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.schemas.doctor import *


class DoctorRepository(BaseRepository):
    @classmethod
    async def get_all(cls, db: AsyncSession, orm_model: Doctor = Doctor) -> list[Doctor]:
        return await super().get_all(db, orm_model)

    @classmethod
    async def get_by_id(cls, db: AsyncSession, id: int, orm_model: Doctor = Doctor) -> Doctor:
        return await super().get_by_id(db, id, orm_model)

    @classmethod
    async def create(cls, db: AsyncSession, create_scheme: DoctorCreate, orm_model: Doctor = Doctor) -> Doctor:
        return await super().create(db, orm_model, create_scheme)

    @classmethod
    async def update(cls, db: AsyncSession, update_scheme: DoctorUpdate, orm_model: Doctor = Doctor) -> Doctor:
        return await super().update(db, orm_model, update_scheme)

    @classmethod
    async def delete(cls, db: AsyncSession, delete_scheme: DoctorDelete, orm_model: Doctor = Doctor):
        return await super().delete(db, orm_model, delete_scheme)
