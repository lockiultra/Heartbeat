from fastapi import APIRouter, Depends
from backend.api.repository.patient import PatientRepository
from backend.api.schemas.patient import *
from backend.core.db import get_db

patient_router = APIRouter()


@patient_router.get('/')
async def get_all_patients(db=Depends(get_db)) -> list[PatientGet]:
    return await PatientRepository.get_all(db)


@patient_router.get('/{id:int}')
async def get_patient_by_id(id: int, db=Depends(get_db)) -> PatientGet:
    return await PatientRepository.get_by_id(db, id)


@patient_router.post('/')
async def create_patient(db=Depends(get_db), create_scheme: PatientCreate = Depends()):
    return await PatientRepository.create(db, create_scheme)


@patient_router.put('/')
async def update_patient(db=Depends(get_db), update_scheme: PatientUpdate = Depends()):
    return await PatientRepository.update(db, update_scheme)


@patient_router.delete('/{id:int}')
async def delete_patient(delete_scheme: PatientDelete = Depends(), db=Depends(get_db)):
    return await PatientRepository.delete(db, delete_scheme)
