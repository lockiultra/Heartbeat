from typing import Type, Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.schemas.appointment import AppointmentCreate, AppointmentUpdate, AppointmentDelete
from backend.api.models.appointment import Appointment
from backend.api.repository.base import BaseRepository


class AppointmentRepository:
    @classmethod
    async def get_by_patient(cls, db: AsyncSession, patient_id: int) -> Sequence[Appointment]:
        appointments = await db.execute(select(Appointment).where(Appointment.patient_id == patient_id))
        return appointments.scalars().all()

    @classmethod
    async def get_by_doctor(cls, db: AsyncSession, doctor_id: int) -> Sequence[Appointment]:
        appointments = await db.execute(select(Appointment).where(Appointment.doctor_id == doctor_id))
        return appointments.scalars().all()

    @classmethod
    async def get_by_id(cls, db: AsyncSession, appointment_id: int) -> Appointment:
        appointment = await db.execute(select(Appointment).where(Appointment.id == appointment_id))
        return appointment.scalars().first()

    @classmethod
    async def create(cls, db: AsyncSession, create_scheme: AppointmentCreate) -> Appointment:
        appointment_data = create_scheme.model_dump()
        appointment = Appointment(**appointment_data)
        db.add(appointment)
        await db.commit()
        await db.refresh(appointment)
        return appointment

    @classmethod
    async def update(cls, db: AsyncSession, update_scheme: AppointmentUpdate) -> Appointment:
        appointment_data = update_scheme.model_dump()
        appointment = await cls.get_by_id(db=db, appointment_id=update_scheme.id)
        for key, value in appointment_data.items():
            if value:
                setattr(appointment, key, value)
        db.add(appointment)
        await db.commit()
        await db.refresh(appointment)
        return appointment

    @classmethod
    async def delete(cls, db: AsyncSession, delete_scheme: AppointmentDelete) -> Appointment:
        appointment = await cls.get_by_id(db=db, appointment_id=delete_scheme.id)
        await db.delete(appointment)
        await db.commit()
        return appointment
    