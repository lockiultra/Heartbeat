from backend.core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator
from backend.api.models.user import User # noqa
from backend.api.models.patient import Patient # noqa
from backend.api.models.base import Base # noqa
from backend.api.models.appointment import Appointment # noqa


engine = create_async_engine(settings.DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


async def create_tables() -> None:
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
