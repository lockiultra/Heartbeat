from backend.api.repository.base import BaseRepository
from backend.api.models.patient import Patient
from backend.api.models.base import Base
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.schemas.patient import *


class PatientRepository(BaseRepository):
    @classmethod
    async def get_all(cls, db: AsyncSession, orm_model: Base = Patient) -> list[Patient]:
        return await super().get_all(db, orm_model)

    @classmethod
    async def get_by_id(cls, db: AsyncSession, id: int, orm_model: Base = Patient) -> Patient:
        return await super().get_by_id(db, id, orm_model)

    @classmethod
    async def create(cls, db: AsyncSession, create_scheme: PatientCreate, orm_model: Base = Patient) -> Patient:
        return await super().create(db, orm_model, create_scheme)

    @classmethod
    async def update(cls, db: AsyncSession, update_scheme: PatientUpdate, orm_model: Base = Patient) -> Patient:
        return await super().update(db, orm_model, update_scheme)

    @classmethod
    async def delete(cls, db: AsyncSession, delete_scheme: PatientDelete, orm_model: Base = Patient) -> Patient:
        return await super().delete(db, orm_model, delete_scheme)