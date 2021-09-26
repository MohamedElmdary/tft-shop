from bottle import HTTPError
from json import dumps


def error(error: HTTPError):
    return dumps({
        'error': 'Something went wrong',
        'status': error.status_code
    })


errors = {
    404: error,
    405: error,
    500: error
}
