from fastapi import HTTPException
from starlette import status

from app.dao.base import BaseDAO
from app.users.models import User


class UsersDAO(BaseDAO):
    model = User

    ROLE_FIELDS = {
        'demo': "is_demo_user",
        'user':  "is_full_user",
        'admin': "is_admin",
    }

    @classmethod
    async def set_role(cls, user_id: int, role: str) -> User:
        """
        Сбрасывает ВСЕ роли на False и устанавливает указанную в True.
        Работает с любым количеством ролей благодаря конвенции именования.
        """
        # 1. Валидация: есть ли такая роль в списке?
        if role not in cls.ROLE_FIELDS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Роль {role} не существует, Доступные роли: {','.join(cls.ROLE_FIELDS)}"
            )

        user = await super().find_one_or_none_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="пользователь не найден"
            )


        target_field = cls.ROLE_FIELDS[role]

        #1. сбрасываем все роли на False

        updated_data = {field: False for field in cls.ROLE_FIELDS.values()}

        #2. Включаем нужную роль
        updated_data[target_field] = True

        return await super().update(filter_by={"id": user_id}, **updated_data)






