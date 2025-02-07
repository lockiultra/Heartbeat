from fastapi import APIRouter, Depends
from backend.api.repository.patient import PatientRepository
from backend.api.schemas.patient import PatientCreate, PatientUpdate, PatientDelete
from backend.api.models.patient import Patient
from backend.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

patient_router = APIRouter()


@patient_router.get('/')
async def get_all_patients(db: AsyncSession = Depends(get_db)):
    return await PatientRepository.get_all(db=db)


@patient_router.get('/{patient_id:int}')
async def get_patient_by_id(patient_id: int, db=Depends(get_db)):
    return await PatientRepository.get_by_id(db=db, id=patient_id)


@patient_router.post('/')
async def create_patient(db=Depends(get_db), create_scheme: PatientCreate = Depends()):
    return await PatientRepository.create(db=db, create_scheme=create_scheme)


@patient_router.put('/')
async def update_patient(db=Depends(get_db), update_scheme: PatientUpdate = Depends()):
    return await PatientRepository.update(db=db, update_scheme=update_scheme)


@patient_router.delete('/')
async def delete_patient(delete_scheme: PatientDelete = Depends(), db=Depends(get_db)):
    return await PatientRepository.delete(db=db, delete_scheme=delete_scheme)
