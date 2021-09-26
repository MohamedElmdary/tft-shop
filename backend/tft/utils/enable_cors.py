from bottle import request, response


def enable_cors(fn):
    """ Using enable_cors with any bottle router enables cors for that router
        by enabling cors this router becomes accessable from front end
        whenever the request method isn't `OPTIONS` the router itself runs.
    """
    def _enable_cors(*args, **kwargs):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, OPTIONS, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"

        if request.method != "OPTIONS":
            return fn(*args, **kwargs)

    return _enable_cors
