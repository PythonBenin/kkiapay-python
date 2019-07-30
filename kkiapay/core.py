import json
from collections import namedtuple

import requests

from kkiapay.exceptions import KKiapayAlogrithmException, KKiapayDestinationTypeException


class Kkiapay:
    BASE_URL = "https://api.kkiapay.me"
    SANDBOX_URL = "https://api-sandbox.kkiapay.me"
    ALGORITHMS = {"1": 'rate', "2": 'roof'}

    RATE_FREQUENCIES = {"1": '3d', "2": '1w', "3": '1m'}
    default_roof_amount = "50000"
    DESTINATION_TYPES = {
        "1": 'MOBILE_MONEY',
        "2": 'BANK_ACCOUNT',
    }

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
        
        try:
            r = requests.post(self.url, data=payload, headers=self.headers)
        except requests.exceptions.ConnectionError:
            return print('Sorry! There is a problem with your connection.')

        return json.loads(
            r.text,
            object_hook=lambda d: namedtuple("KkiapayTransaction", d.keys())(
                *d.values()
            ),
        )

    def refund_transaction(self, transaction_id):
        self.url += "/api/v1/transactions/revert"
        payload = {"transactionId": transaction_id}
        
        try:
            r = requests.post(self.url, data=payload, headers=self.headers)
        except requests.exceptions.ConnectionError:
            return print('Sorry! There is a problem with your connection.')

        return json.loads(
            r.text,
            object_hook=lambda d: namedtuple("KkiapayTransaction", d.keys())(
                *d.values()
            ),
        )

    def setup_payout(self, algorithm: str, destination: str, destination_type: str, roof_amount: str = None,
                     send_notification: bool = True, rate_frequency: str = RATE_FREQUENCIES["1"],
                     country_code: str = "229"):
        options = {
            "destination": country_code + destination if destination_type == "1" else destination,
            "send_notification": 1 if send_notification else 0,
        }

        if destination_type in self.DESTINATION_TYPES.keys():
            options["destination_type"] = self.DESTINATION_TYPES[destination_type]
        else:
            raise KKiapayDestinationTypeException(self.DESTINATION_TYPES)

        if algorithm in self.ALGORITHMS.keys():
            options['algorithm'] = self.ALGORITHMS[algorithm]
        else:
            raise KKiapayAlogrithmException(self.ALGORITHMS)
        if algorithm == "2":
            options["roof_amount"] = roof_amount if roof_amount is not None else self.default_roof_amount
        else:
            options["rate_frequency"] = rate_frequency if rate_frequency in self.RATE_FREQUENCIES.values() else \
                self.RATE_FREQUENCIES["1"]
        r = requests.post(self.url + '/merchant/payouts/schedule', data=options, headers=self.headers)
        return {
            'response': r.json(),
            'status_code': r.status_code
        }
