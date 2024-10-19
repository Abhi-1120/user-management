from app.manage import create_app

app, router = create_app()

from .api import *

# Include API routes
app.include_router(router)
