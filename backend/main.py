from bottle import Bottle


routes = Bottle()


@routes.get("/address")
def get_address_handler():
    return {
        'hello': 'world'
    }


""" init app """
app = Bottle()
app.mount("/tft-shop/api", routes)


app.run(port=3000, reloader=True)
