from backend.api.models.user import User
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Patient(User):
    insurance: Mapped[str] = mapped_column(String, nullable=False)
