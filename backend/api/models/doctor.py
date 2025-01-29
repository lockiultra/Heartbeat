from backend.api.models.user import User
from enum import Enum
from sqlalchemy.orm import Mapped


class DOCTOR_SPEC(str, Enum):
    CARDIO = "Cardio"
    DERMATOLOGIST = "Dermatologist"
    ENDOCRINOLOGIST = "Endocrinologist"
    GASTROENTEROLOGIST = "Gastroenterologist"
    NEUROLOGIST = "Neurologist"
    ONCOLOGIST = "Oncologist"
    OPHTHALMOLOGIST = "Ophthalmologist"
    PEDIATRICIAN = "Pediatrician"
    PSYCHIATRIST = "Psychiatrist"
    UROLOGIST = "Urologist"


class Doctor(User):
    __abstract__ = False

    speciality: Mapped[DOCTOR_SPEC]
