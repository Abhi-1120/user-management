import aiomysql
from aiomysql.cursors import DictCursor

from app import app


async def connect_mysql():
    return await aiomysql.connect(host=app.config.MYSQL_DATABASE_HOST, port=app.config.MYSQL_DATABASE_PORT,
                                  user=app.config.MYSQL_DATABASE_USER, password=app.config.MYSQL_DATABASE_PASSWORD,
                                  db=app.config.MYSQL_DATABASE, cursorclass=DictCursor)


class MysqlConnectionManager:
    def __init__(self):
        self.conn = None

    async def __aenter__(self):
        self.conn = await connect_mysql()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
