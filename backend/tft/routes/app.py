from bottle import Bottle
from tft.utils.enable_cors import enable_cors
from tft.utils.errors import errors
# from uuid import uuid4
from threading import Timer
import requests
from json import loads
from jumpscale.loader import j

app_routes = Bottle()
app_routes.error_handler = errors


BITCOIN_WALLET_ADDRESS = "tb1qu0423d0x7uzvx2qt5dh9f75z0em5ls9fu0wqhq"
TFT_WALLET = j.clients.stellar.get('ayoub')

# load wallet balance
# TFT_WALLET.get_balance()


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

    transactions = {}
    for transaction in TFT_WALLET.list_transactions():
        _txid = transaction.memo_text
        if type(_txid) is str:
            transactions[_txid] = True

    for tx in txs:
        txid = tx.get('txid')

        if not tx.get('status').get('confirmed') or txid in transactions:
            print('Sent!')
            continue

        amount = [
            v.get('value') for v in tx.get('vout') if v.get('scriptpubkey_address') == BITCOIN_WALLET_ADDRESS
        ]
        if len(amount) == 0:
            continue

        sent_amount = amount[0] / 1e8
        vin = tx.get("vin")[0]
        target_address = vin.get("prevout").get("scriptpubkey_address")

        amount = 0.1  # sent_amount * factor

        print('Sending')
        TFT_WALLET.transfer(
            destination_address=target_address,
            amount=amount,
            asset="XLM",
            memo_text=txid
        )

    _start_pool()


_start_pool()
