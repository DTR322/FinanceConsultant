from sqlalchemy import select, delete, update
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.scalars().all()


    @classmethod
    async def find_one_or_none_by_id(cls, data_id):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(id=data_id)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)

            await session.refresh(new_instance)
            return new_instance


    @classmethod
    async def update(cls, filter_by , **values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    update(cls.model)
                    .filter_by(**filter_by)
                    .values(**values)
                    .execution_options(synchronize_session='fetch')
                )
                result = await session.execute(query)
                return result.rowcount


    @classmethod
    async def delete(cls,  delete_all: bool = False, **filter_by):
        if not delete_all and not filter_by:
            raise ValueError("Необходимо указать хотя бы 1 параметр для удаления")

        async with (async_session_maker() as session):
            async with session.begin():
                query = (
                    delete(cls.model)
                    .filter_by(**filter_by)
                )
                result = await session.execute(query)
                return result.rowcount