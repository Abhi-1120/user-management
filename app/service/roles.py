from app.common import get_current_datetime
from app.core import MysqlConnectionManager
from app.core.mysql.roles import (add_role, get_total_role_count, get_total_role, get_role_details_by_role_id,
                                  update_role_details, delete_role_by_role_id, add_access_module,
                                  delete_access_module_for_role_id)


__all__ = ["CreateRoleService", "RoleListService", "GetRoleService", "UpdateRoleService", "DeleteRoleService"]


class CreateRoleService:
    def __init__(self, payload):
        self.payload = payload
        self.role_id = None

    async def create_role(self):
        async with MysqlConnectionManager() as conn:
            self.role_id = await self.add_role(conn)
            await self.add_access_module(conn)
            await conn.commit()
        return {"ok": True, "id": self.role_id}

    async def add_role(self, conn):
        payload = {
            "role_name": self.payload.role_name,
            "active": self.payload.active,
            "created_at": get_current_datetime(),
        }
        return await add_role(conn, payload)

    async def add_access_module(self, conn):
        payload = {
            "role_id": self.role_id,
            "access_modules": self.payload.access_modules,
            "created_at": get_current_datetime(),
        }
        return await add_access_module(conn, payload)


class RoleListService:
    def __init__(self, payload):
        self.payload = payload

    async def roles_list(self):
        async with MysqlConnectionManager() as conn:
            self.payload.search = f"%{self.payload.search}%"
            total = await get_total_role_count(conn, self.payload)
            role_list = await get_total_role(conn, self.payload)
        return {
            "total": total,
            "roles": role_list
        }


class GetRoleService:
    def __init__(self, role_id):
        self.role_id = role_id

    async def get_role(self):
        async with MysqlConnectionManager() as conn:
            role_details = await get_role_details_by_role_id(conn, self.role_id)
        return role_details


class UpdateRoleService:
    def __init__(self, role_id, payload):
        self.role_id = role_id
        self.payload = payload

    async def update_role(self):
        async with MysqlConnectionManager() as conn:
            await self.update_role_details(conn)
            await conn.commit()
        return {"ok": True, "id": self.role_id}

    async def update_role_details(self, conn):
        payload = {
            "role_name": self.payload.role_name,
            "active": self.payload.active,
            "role_id": self.role_id
        }
        await update_role_details(conn, payload)
        await delete_access_module_for_role_id(conn, self.role_id)
        await add_access_module(conn, payload)


class DeleteRoleService:
    def __init__(self, role_id):
        self.role_id = role_id

    async def delete_role(self):
        async with MysqlConnectionManager() as conn:
            await delete_access_module_for_role_id(conn, self.role_id)
            await delete_role_by_role_id(conn, self.role_id)
            await conn.commit()
        return {"ok": True, "id": self.role_id}
