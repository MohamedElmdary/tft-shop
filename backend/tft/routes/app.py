from bottle import Bottle
from tft.utils.enable_cors import enable_cors
from tft.utils.errors import errors
# from uuid import uuid4
from threading import Timer
import requests
from json import loads

app_routes = Bottle()
app_routes.error_handler = errors


BITCOIN_WALLET_ADDRESS = "tb1qu0423d0x7uzvx2qt5dh9f75z0em5ls9fu0wqhq"
# MEMPOOL = []


@app_routes.get("/address")
@enable_cors
def get_address_handler():
    # global MEMPOOL

    # id = str(uuid4())
    # MEMPOOL.append(id)

    return {
        'address': BITCOIN_WALLET_ADDRESS
        # ,'message': id
    }


"""
# pooling for txs
"""


def _start_pool():
    Timer(5.0, pooling).start()


API = f"https://blockstream.info/testnet/api/address/{BITCOIN_WALLET_ADDRESS}/txs"


def pooling():
    res = requests.get(API)
    if res.status_code != 200:
        return _start_pool()

    txs = loads(res.content)

    # Get stellar txs
    # And convert them into hashmap for O(1) accessing

    for tx in txs:
        if not tx.get('status').get('confirmed'):
            continue
        txid = str.join('-', [t.get('txid') for t in tx.get('vin')])
        vout = [
            v.get('value') for v in tx.get('vout') if v.get('scriptpubkey_address') == BITCOIN_WALLET_ADDRESS
        ][0] / 1e8

        print(txid, vout)

    _start_pool()


_start_pool()
