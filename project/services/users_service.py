from typing import Optional

from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """Сервис получения одного пользователя"""

        return self.dao.get_one(uid)

    def get_by_email(self, email):
        """Сервис получения пользователей по email"""

        return self.dao.get_by_email(email)


    def get_all(self):
        """Сервис получения всех пользователя"""
        users = self.dao.get_all()
        return users


    def create(self, user_d: dict[str, str]):
        """Сервис создания пользователя"""

        user_d["password"] = generate_password_hash(user_d["Password"])
        return self.dao.create(user_d)


    def update(self, user_d):
        """Сервис обновления пользователя"""


        return self.dao.update(user_d)

    def update_password(self, email, new_password):
        """Сервис обновления пароля пользователя"""

        return self.dao.update_password(email, new_password)


    def delete(self, uid):
        """Сервис удаления пользователя"""

        return self.dao.delete(uid)
