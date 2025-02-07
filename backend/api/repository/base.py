from typing import Type, Sequence
from backend.core.db import Base
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.schemas.user import *
from backend.core.auth import get_password_hash
from backend.api.models.user import User
from fastapi import HTTPException, status


class BaseRepository:
    @classmethod
    async def get_all(cls, db: AsyncSession, orm_model: Type[Base]) -> Sequence[Base]:
        result = await db.execute(select(orm_model))
        return result.scalars().all()

    @classmethod
    async def get_by_id(cls, db: AsyncSession, id: int, orm_model: Type[Base]) -> User:
        result = await db.execute(select(orm_model).where(orm_model.id == id))
        result = result.scalars().first()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        return result

    @classmethod
    async def create(cls, db: AsyncSession, orm_model: Type[Base], create_scheme: UserCreate)  -> User:
        data = create_scheme.model_dump()
        new_model = orm_model(**data)
        new_model.password = get_password_hash(new_model.password)
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @classmethod
    async def update(cls, db: AsyncSession, orm_model: Type[Base], update_scheme: UserUpdate) -> User:
        data = update_scheme.model_dump()
        model = await cls.get_by_id(db, update_scheme.id, orm_model)
        for key, value in data.items():
            if value:
                if key == 'password':
                    value = get_password_hash(value)
                setattr(model, key, value)
        db.add(model)
        await db.commit()
        await db.refresh(model)
        return model

    @classmethod
    async def delete(cls, db: AsyncSession, orm_model: Type[Base], delete_scheme: UserDelete) -> User:
        model = await cls.get_by_id(db, delete_scheme.id, orm_model)
        await db.delete(model)
        await db.commit()
        return model
