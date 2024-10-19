import os
from jose import jwt
from io import StringIO
from configparser import ConfigParser
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from datetime import timedelta, datetime, timezone
from app.common.errors import errors


def custom_exception_handler(req, exc):
    """ Custom exception handler
    :param req - Request object
    :param exc - Exception

    :returns - Define error message for custom exception
    """

    # req.app.logger.info(f"Custom Exception {exc.__class__.__name__} on {req.url.path}")
    return JSONResponse(content=errors.get(exc.__class__.__name__, errors['Exception']),
                        status_code=errors.get(exc.__class__.__name__, errors['Exception'])['status'])


def read_properties_file(file_path):
    with open(file_path) as f:
        config = StringIO()
        config.write('[dummy_section]\n')
        config.write(f.read().replace('%', '%%'))
        config.seek(0, os.SEEK_SET)
        cp = ConfigParser()
        cp.read_file(config)
        return dict(cp.items('dummy_section'))


def create_token(payload, expires_delta: timedelta = None):
    from app import app
    # Calculate token expiration time
    if expires_delta:
        expire_datetime = datetime.utcnow() + expires_delta
    # Create payload with username and expiration time
    payload['exp'] = expire_datetime
    # Generate JWT token
    token = jwt.encode(payload, app.config.SECRET_KEY, algorithm=app.config.JWT_ALGORITHM)
    return token


def get_current_datetime():
    return datetime.now(timezone.utc)


def hash_password(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)
