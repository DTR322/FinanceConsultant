from typing import Any

from app.dao.base import BaseDAO
from app.wallets.models import Wallet




class WalletsDAO(BaseDAO):
    model = Wallet

    # ни в коем случае не переопределяйте model ниже
    @classmethod
    async def add(cls, user_id: int, **values) -> model:
        return await super().add(**{**values, "user_id": user_id})


    @classmethod
    async def find_all(cls, user_id: int, **filter_by) -> list[model]:
        return await super().find_all(**{**filter_by, "user_id": user_id})


    @classmethod
    async def find_one_or_none(cls, user_id: int, **filter_by) -> model | None:
        return await super().find_one_or_none(**{**filter_by, "user_id": user_id})


    # так и запланировано
    @classmethod
    async def update(cls, wallet_id: int, user_id: int, **values) -> int:
        # BaseDAO.update принимает filter_by как dict, а не **kwargs
        filters ={"id": wallet_id, "user_id": user_id}

        return await super().update(filters, **values)


    @classmethod
    async def delete(cls, user_id: int, delete_all: bool = False, **filter_by) -> int:

        filter_by["user_id"]=user_id

        return await super().delete(**filter_by)