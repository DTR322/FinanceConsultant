from pydantic import EmailStr, Field, ConfigDict, field_validator, BaseModel
from typing import Literal


class SUserRegister(BaseModel):
    """
    Схема для регистрации.
    Ничего лишнего: только почта для входа и пароль для защиты.
    """
    email: EmailStr = Field(..., description="Email для входа")
    # Для финансов пароль должен быть надежнее. Ставим min_length=8
    password: str = Field(..., min_length=8, max_length=50, description="Пароль (мин. 8 символов)")

    @field_validator("password")
    @classmethod
    def check_password_complexity(cls, value: str):
        if value.isdigit():
            raise ValueError("Пароль не должен состоять только из цифр")
        return value


class SUserAuth(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")


class SUserResponse(BaseModel):
    """
    Что мы возвращаем клиенту после регистрации.
    Пароль не возвращаем никогда!
    """
    id: int
    email: EmailStr
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)  # Важно для ORM -> Pydantic конвертации


class SRoleUpdate(BaseModel):

    role: Literal["demo", "user", "admin"] = Field(...,
                                                   description="Новая роль пользователя")