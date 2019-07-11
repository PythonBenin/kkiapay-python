import requests


class Kkiapay:
    BASE_URL = 'https://api.kkiapay.me'
    SANDBOX_URL = 'https://api-sandbox.kkiapay.me'

    def __init__(self, public_key, private_key, secret, sandbox=False):
        self.public_key = public_key
        self.private_key = private_key
        self.secret = secret
        self.sandbox = sandbox

    def verify_transaction(self, transaction_id):
        url = self.SANDBOX_URL if self.sandbox else self.BASE_URL
        url += '/api/v1/transactions/status'
        payload = {'transactionId': transaction_id}
        headers = {'Accept': 'application/json', 'X-API-KEY': self.public_key, 'X-PRIVATE-KEY': self.private_key, 'X-SECRET-KEY': self.secret}

        r = requests.post(url, data=payload, headers=headers)
        return r.json()

    def refund_transaction(self, transaction_id):
        url = self.SANDBOX_URL if self.sandbox else self.BASE_URL
        url += '/api/v1/transactions/revert'
        payload = {'transactionId': transaction_id}
        headers = {'Accept': 'application/json', 'X-API-KEY': self.public_key, 'X-PRIVATE-KEY': self.private_key, 'X-SECRET-KEY': self.secret}

        r = requests.post(url, data=payload, headers=headers)
        return r.json()