"""Main module."""

from . import api_router
from .app import app
from .routes import backend_router

app.include_router(api_router)
app.include_router(backend_router)
