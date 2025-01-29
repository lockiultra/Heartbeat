from backend.core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from backend.api.models.user import User # noqa
from backend.api.models.patient import Patient # noqa
from backend.api.models.base import Base # noqa


engine = create_async_engine(settings.DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db() -> AsyncSession:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


async def create_tables():
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)