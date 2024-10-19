import pymysql
from app.core import sql_scripts
from app.common import RoleAlreadyExistException, RoleNotFoundException

__all__ = ["add_role", "get_total_role_count", "get_total_role", "get_role_details_by_role_id", "update_role_details",
           "delete_role_by_role_id", "add_access_module", "delete_access_module_for_role_id"]


async def add_role(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["add_role"], payload)
        return cursor.lastrowid
    except pymysql.err.IntegrityError:
        raise RoleAlreadyExistException


def add_access_module(conn, payload):
    with conn.cursor() as cursor:
        sql_stmt = sql_scripts['add_access_module']
        params = [{
            "role_id": payload["role_id"],
            "module": module,
            "created_at": payload["created_at"]
        } for module in payload["access_modules"]]

        cursor.executemany(sql_stmt, params)


async def get_total_role_count(conn, payload):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_total_role_count"], payload)
        row = await cursor.fetchone()
        if row:
            return row.get('total')
        return 0


async def get_total_role(conn, payload):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_total_role"], payload)
        rows = await cursor.fetchall()
        if rows:
            return rows
        return []


async def get_role_details_by_role_id(conn, role_id):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_role_by_role_id"], {"role_id": role_id})
        row = await cursor.fetchone()
        if row:
            return row
        return None


async def update_role_details(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["update_role_details"], payload)
    except pymysql.err.IntegrityError:
        raise RoleNotFoundException


async def delete_role_by_role_id(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["delete_role"], payload)
    except pymysql.err.IntegrityError:
        raise RoleNotFoundException


async def delete_access_module_for_role_id(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["delete_access_module_for_role_id"], payload)
    except pymysql.err.IntegrityError:
        raise RoleNotFoundException
