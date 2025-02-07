from backend.api.models.base import Base
from backend.api.models.doctor import Doctor
from backend.api.models.patient import Patient
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Integer, String, ForeignKey, DateTime
from datetime import datetime


class Appointment(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('doctor.id'), nullable=False)
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey('patient.id'), nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    doctor: Mapped[Doctor] = relationship('Doctor', back_populates='appointments')
    patient: Mapped[Patient] = relationship('Patient', back_populates='appointments')
