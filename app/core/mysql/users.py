import pymysql
from app.core import sql_scripts
from app.common import UserAlreadyExistException, UserNotFoundException, hash_password

__all__ = ["add_user", "get_total_user_count", "get_total_user", "get_user_details_by_user_id", "update_user_details",
           "update_password_for_user", "bulk_update_user_info", "delete_user_by_user_id", "check_user_module_access"]


async def add_user(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["add_user"], payload)
        return cursor.lastrowid
    except pymysql.err.IntegrityError:
        raise UserAlreadyExistException


async def get_total_user_count(conn, payload):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_total_user_count"], payload)
        row = await cursor.fetchone()
        if row:
            return row.get('total')
        return 0


async def get_total_user(conn, payload):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_total_user"], payload)
        rows = await cursor.fetchall()
        if rows:
            return rows
        return []


async def get_user_details_by_user_id(conn, user_id):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_user_by_user_id"], {"user_id": user_id})
        row = await cursor.fetchone()
        if row:
            return row
        return None


async def update_user_details(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["update_user_details"], payload)
    except pymysql.err.IntegrityError:
        raise UserNotFoundException


async def update_password_for_user(conn, payload):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["update_user_password"], payload)


async def bulk_update_user_info(conn, user_data):
    async with conn.cursor() as cursor:
        sql_stmt = sql_scripts["bulk_update_user"]

        first_name = []
        last_name = []
        email = []
        password = []
        role = []
        user_ids = []

        for user in user_data:
            user_id = user["user_id"]
            user_ids.append(str(user_id))
            if "first_name" in user:
                first_name.append(f"WHEN {user_id} THEN '{user['first_name']}'")
            if "last_name" in user:
                last_name.append(f"WHEN {user_id} THEN '{user['last_name']}'")
            if "email" in user:
                email.append(f"WHEN {user_id} THEN '{user['email']}'")
            if "password" in user:
                password.append(f"WHEN {user_id} THEN '{hash_password(user['password'])}'")
            if "role" in user:
                role.append(f"WHEN {user_id} THEN '{user['role']}'")

        if first_name:
            sql_stmt += f"first_name = CASE {' '.join(first_name)} END, "
        if last_name:
            sql_stmt += f"last_name = CASE {' '.join(last_name)} END, "
        if email:
            sql_stmt += f"email = CASE {' '.join(email)} END, "
        if password:
            sql_stmt += f"password = CASE {' '.join(password)} END, "
        if role:
            sql_stmt += f"role = CASE {' '.join(role)} END, "

        query = sql_stmt.rstrip(", ")
        query += f" WHERE user_id IN ({', '.join(user_ids)});"

        await cursor.execute(query)


async def delete_user_by_user_id(conn, payload):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql_scripts["delete_user"], payload)
    except pymysql.err.IntegrityError:
        raise UserNotFoundException


async def check_user_module_access(conn, user_id, module_name):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_module_by_user_id"], {"user_id": user_id, "module_name": module_name})
        row = await cursor.fetchone()
        if row:
            return row.get('total')
        return 0
