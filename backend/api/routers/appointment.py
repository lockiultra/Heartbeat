from fastapi import APIRouter, Depends
from backend.core.db import get_db
from backend.api.repository.appointment import AppointmentRepository
from backend.api.schemas.appointment import AppointmentCreate, AppointmentUpdate, AppointmentDelete
from sqlalchemy.ext.asyncio import AsyncSession


appointment_router = APIRouter()


@appointment_router.get('/by_doctor/{doctor_id: int}')
async def get_by_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    return await AppointmentRepository.get_by_doctor(db=db, doctor_id=doctor_id)


@appointment_router.get('/by_patient/{patient_id: int}')
async def get_by_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    return await AppointmentRepository.get_by_patient(db=db, patient_id=patient_id)


@appointment_router.get('/by_id/{appointment_id: int}')
async def get_by_id(appointment_id: int, db: AsyncSession = Depends(get_db)):
    return await AppointmentRepository.get_by_id(db=db, appointment_id=appointment_id)


@appointment_router.post('/')
async def create_appointment(create_scheme: AppointmentCreate = Depends(), db: AsyncSession = Depends(get_db)):
    return await AppointmentRepository.create(db=db, create_scheme=create_scheme)


@appointment_router.put('/')
async def update_appointment(update_scheme: AppointmentUpdate = Depends(), db: AsyncSession = Depends(get_db)):
    return await AppointmentRepository.update(db=db, update_scheme=update_scheme)


@appointment_router.delete('/')
async def delete_appointment(delete_scheme: AppointmentDelete = Depends(), db: AsyncSession = Depends(get_db)):
    return await AppointmentRepository.delete(db=db, delete_scheme=delete_scheme)
