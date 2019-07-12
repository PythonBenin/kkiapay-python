import json
import requests
from collections import namedtuple
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


class Kkiapay:

    BASE_URL = "https://api.kkiapay.me"
    SANDBOX_URL = "https://api-sandbox.kkiapay.me"

    def __init__(self, public_key, private_key, secret, sandbox=False):
        self.secret = secret
        self.sandbox = sandbox
        self.public_key = public_key
        self.private_key = private_key
        self.headers = {
            "Accept": "application/json",
            "X-SECRET-KEY": self.secret,
            "X-API-KEY": self.public_key,
            "X-PRIVATE-KEY": self.private_key,
        }
        self.url = self.SANDBOX_URL if self.sandbox else self.BASE_URL


    def verify_transaction(self, transaction_id):
        self.url += "/api/v1/transactions/status"
        payload = {"transactionId": transaction_id}
        r = requests.post(self.url, data=payload, headers=self.headers)

        return json.loads(r.text, object_hook=lambda d: namedtuple('KkiapayTransaction', d.keys())(*d.values()))

    def refund_transaction(self, transaction_id):
        self.url += "/api/v1/transactions/revert"
        payload = {"transactionId": transaction_id}
        r = requests.post(self.url, data=payload, headers=self.headers)
        return r.text

    def setup_payout(self, options):
        self.url += "/merchant/payouts/schedule"
        r = requests.post(self.url, data=options, headers=self.headers)
        return r.text