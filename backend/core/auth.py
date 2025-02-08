import jwt
from passlib.context import CryptContext
from datetime import datetime, UTC, timedelta
from backend.core.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.api.models.patient import Patient
from backend.api.models.doctor import Doctor


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


async def authenticate_user(db: AsyncSession, username: str, password: str):
    result = await db.execute(select(Patient).where(Patient.username == username))
    user = result.scalars().first()
    if user and verify_password(password, user.password):
        return user
    result = await db.execute(select(Doctor).where(Doctor.username == username))
    user = result.scalars().first()
    if user and verify_password(password, user.password):
        return user
    return None
