from inspect import getmembers, isclass
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import app.common.exceptions as exceptions
from app.common.utils import custom_exception_handler
from .config import Config


def create_app():
    """Create fastAPI app"""

    app = FastAPI(title=__name__)
    router = APIRouter(prefix='')
    app.config = Config()
    add_cross_origins(app)
    map_exception_handlers(app)
    return app, router


def map_exception_handlers(app):
    """ Map all custom exceptions with application """

    # Custom exception binding

    business_exception = dict(getmembers(exceptions, isclass))
    [app.add_exception_handler(exception_class, custom_exception_handler)
     for exception, exception_class in business_exception.items() if exception in exceptions.__all__]

    # Handle Internal Server Error
    # app.add_exception_handler(Exception, exception_handler)


def add_cross_origins(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
