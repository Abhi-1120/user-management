from app.common import get_current_datetime, hash_password
from app.core import MysqlConnectionManager
from app.core.mysql.users import (add_user, get_total_user_count, get_total_user, get_user_details_by_user_id,
                                  update_user_details, update_password_for_user, bulk_update_user_info,
                                  delete_user_by_user_id, check_user_module_access)

__all__ = ["CreateUserService", "UserListService", "GetUserService", "UpdateUserService", "BulkUpdateUserService",
           "DeleteUserService", "UserModuleAccessService"]


class CreateUserService:
    def __init__(self, payload):
        self.payload = payload
        self.user_id = None

    async def create_user(self):
        async with MysqlConnectionManager() as conn:
            self.user_id = await self.add_user(conn)
            await conn.commit()
        return {"ok": True, "id": self.user_id}

    async def add_user(self, conn):
        password = hash_password(self.payload.password)
        payload = {
            "first_name": self.payload.first_name,
            "last_name": self.payload.last_name,
            "email": self.payload.email,
            "password": password,
            "created_at": get_current_datetime(),
        }
        return await add_user(conn, payload)


class UserListService:
    def __init__(self, payload):
        self.payload = payload

    async def users_list(self):
        async with MysqlConnectionManager() as conn:
            self.payload.search = f"%{self.payload.search}%"
            total = await get_total_user_count(conn, self.payload)
            user_list = await get_total_user(conn, self.payload)
        return {
            "total": total,
            "users": user_list
        }


class GetUserService:
    def __init__(self, user_id):
        self.user_id = user_id

    async def get_user(self):
        async with MysqlConnectionManager() as conn:
            user_details = await get_user_details_by_user_id(conn, self.user_id)
        return user_details


class UpdateUserService:
    def __init__(self, user_id, payload):
        self.user_id = user_id
        self.payload = payload

    async def update_user(self):
        async with MysqlConnectionManager() as conn:
            await self.update_user_details(conn)
            await conn.commit()
        return {"ok": True, "id": self.user_id}

    async def update_user_details(self, conn):
        payload = {
            "first_name": self.payload.first_name,
            "last_name": self.payload.last_name,
            "email": self.payload.email,
            "user_id": self.user_id
        }
        await update_user_details(conn, payload)
        if self.payload.password:
            payload = {
                "password": hash_password(self.payload.password),
                "user_id": self.user_id
            }
            await update_password_for_user(conn, payload)


class BulkUpdateUserService:
    def __init__(self, payload):
        self.payload = payload

    async def bulk_update_user(self):
        async with MysqlConnectionManager() as conn:
            await bulk_update_user_info(conn, self.payload)
            await conn.commit()
        return {"ok": True}


class DeleteUserService:
    def __init__(self, user_id):
        self.user_id = user_id

    async def delete_user(self):
        async with MysqlConnectionManager() as conn:
            await delete_user_by_user_id(conn, self.user_id)
            await conn.commit()
        return {"ok": True, "id": self.user_id}


class UserModuleAccessService:
    def __init__(self, user_id, module_name):
        self.user_id = user_id
        self.module_name = module_name

    async def validate_user_module_access(self):
        async with MysqlConnectionManager() as conn:
            user_access = await check_user_module_access(conn, self.user_id, self.module_name)
            if user_access:
                return {"message": "User has access to selected module"}
        return {"message": "User does not have access to selected module"}
