from bottle import Bottle
from tft.utils.errors import errors
from .routes.app import app_routes


app = Bottle()
app.error_handler = errors

app.mount("/api", app_routes)
