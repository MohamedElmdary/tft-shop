"""
What exactly should be done ?

1) Ui should be able to get address []
2) Ui should notify backend whenever user generats a new QRCode []
3) Server should check if user a new tx was created from "https://github.com/Blockstream/esplora/blob/master/API.md#get-addressaddresstxs"
4) Server should pool for 1 min to check if it was created or not
5) If server found tx it should return back with enough tft
6) Server should expose bitcoin to tft price
"""

from tft.main import app

app.run(port=3000)
