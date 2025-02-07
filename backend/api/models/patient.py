from backend.api.models.user import User
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Patient(User):
    insurance: Mapped[str] = mapped_column(String, nullable=False)

    appointments: Mapped[list['Appointment']] = relationship('Appointment', back_populates='patient')
