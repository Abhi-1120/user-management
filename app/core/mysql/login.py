from ...core import sql_scripts

__all__ = ['get_user']


async def get_user(conn, email):
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["get_user"], {"email": email})
        result = await cursor.fetchone()
        return result
