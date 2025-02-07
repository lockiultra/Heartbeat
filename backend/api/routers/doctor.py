from fastapi import APIRouter, Depends
from backend.api.repository.doctor import DoctorRepository
from backend.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorDelete # noqa
from backend.api.models.doctor import Doctor


doctor_router = APIRouter()


@doctor_router.get('/')
async def get_all_doctors(db: AsyncSession = Depends(get_db)) -> list[Doctor]:
    return await DoctorRepository.get_all(db=db)


@doctor_router.get('/{doctor_id:int}')
async def get_doctor_by_id(doctor_id: int, db: AsyncSession = Depends(get_db)) -> Doctor:
    return await DoctorRepository.get_by_id(db=db, id=doctor_id)


@doctor_router.post('/')
async def create_doctor(create_scheme: DoctorCreate = Depends(), db: AsyncSession = Depends(get_db)) -> Doctor:
    return await DoctorRepository.create(db=db, create_scheme=create_scheme)


@doctor_router.put('/')
async def update_doctor(update_scheme: DoctorUpdate = Depends(), db: AsyncSession = Depends(get_db)) -> Doctor:
    return await DoctorRepository.update(db=db, update_scheme=update_scheme)


@doctor_router.delete('/')
async def delete_doctor(delete_scheme: DoctorDelete = Depends(), db: AsyncSession = Depends(get_db)) -> Doctor:
    return await DoctorRepository.delete(db=db, delete_scheme=delete_scheme)
