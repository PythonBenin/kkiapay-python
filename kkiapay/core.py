import json
import requests
from collections import namedtuple


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
        self.transaction_url = self.url + "/api/v1/transactions/status"
        self.revert_url = self.url + "/api/v1/transactions/revert"
        self.payout_url = self.url + "/merchant/payouts/schedule"

    def verify_transaction(self, transaction_id):
        payload = {"transactionId": transaction_id}
        r = requests.post(self.transaction_url, data=payload, headers=self.headers)

        return json.loads(
            r.text,
            object_hook=lambda d: namedtuple("KkiapayTransaction", d.keys())(
                *d.values()
            ),
        )

    def refund_transaction(self, transaction_id):
        payload = {"transactionId": transaction_id}
        r = requests.post(self.url, data=payload, headers=self.headers)

        return json.loads(
            r.text,
            object_hook=lambda d: namedtuple("KkiapayTransaction", d.keys())(
                *d.values()
            ),
        )

    def setup_payout(self, options):
        r = requests.post(self.payout_url, data=options, headers=self.headers)
        return r.text
