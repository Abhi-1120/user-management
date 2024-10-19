from app import app
from jose import jwt
from datetime import timedelta
from passlib.context import CryptContext
from app.common.utils import create_token
from app.core import MysqlConnectionManager, get_user
from app.common import Token, InvalidUserException, InvalidPasswordException, InvalidTokenException

__all__ = ["LoginService", "GetRefreshedAccessToken"]


class LoginService:
    def __init__(self, payload):
        self.payload = payload
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def do_process(self):
        user = await self.get_data_from_mysql()
        if not user:
            raise InvalidUserException
        password = user.get('password')
        is_correct_password = self.verify_password(password)
        if not is_correct_password:
            raise InvalidPasswordException
        access_token = create_token(user, timedelta(hours=3))
        refresh_token = create_token(user, timedelta(days=30))
        return Token(access_token=access_token, token_type="bearer", refresh_token=refresh_token,
                     user_id=user.get('id'))

    def verify_password(self, password):
        return self.pwd_context.verify(self.payload.password, password)

    async def get_data_from_mysql(self):
        async with MysqlConnectionManager() as conn:
            return await get_user(conn, self.payload.email)


class GetRefreshedAccessToken:
    def __init__(self, refresh_token):
        self.refresh_token = refresh_token

    def do_process(self):
        payload = self.verify_refresh_token()
        if not payload.get('id'):
            raise InvalidTokenException
        access_token = create_token(payload, expires_delta=timedelta(minutes=app.config.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = create_token(payload, timedelta(minutes=app.config.REFRESH_TOKEN_EXPIRE_MINUTES))
        result = {
            "access_token": access_token,
            "token_type": "bearer",
            "refresh_token": refresh_token
        }
        return result

    def verify_refresh_token(self):
        try:
            payload = jwt.decode(self.refresh_token.token, app.config.SECRET_KEY, algorithms=[app.config.JWT_ALGORITHM])
            # Here you can perform additional checks if needed,
            # such as checking if the user exists in the database
            # or checking if the token has expired.
            # For simplicity, I'm just returning the payload.
            return payload
        except jwt.JWTError:
            raise InvalidTokenException
