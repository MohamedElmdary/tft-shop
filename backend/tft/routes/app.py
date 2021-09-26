from bottle import Bottle
from tft.utils.enable_cors import enable_cors
from tft.utils.errors import errors


app_routes = Bottle()
app_routes.error_handler = errors


@enable_cors
@app_routes.get("/address")
def get_address_handler():
    return {
        'address': 0x0533
    }


@enable_cors
@app_routes.post("/notify")
def post_notify_handler():
    return {
        'notify': True
    }
