from requests import request

from .utils import DEFAULT_ROOF_AMOUNT, DESTINATION_TYPES, ALGORITHMS, RATE_FREQUENCIES
from .exceptions import KKiapayAlgorithmException, KKiapayDestinationTypeException


class Kkiapay:
    version = '1'

    def __init__(
            self,
            public_key,
            private_key,
            secret,
            sandbox=False,
            version='1',
            verify_ssl=True,
            timeout=5,
            default_roof_amount=None
    ):
        self.secret = secret
        self.sandbox = sandbox
        self.public_key = public_key
        self.private_key = private_key
        self.verify_ssl = verify_ssl
        self.version = version
        self.timeout = timeout
        self.roof_amount = default_roof_amount or DEFAULT_ROOF_AMOUNT
        self.is_api = False

    def _get_url(self, endpoint):
        url = f"https://api.kkiapay.me"
        if self.sandbox:
            url = "https://api-sandbox.kkiapay.me"

        if endpoint.startswith('/'):
            endpoint = endpoint[1:]

        if self.is_api:
            url = f'{url}/api/{self.version}'

        return f'{url}/{endpoint}'

    def _request(self, method, endpoint, data, params=None, **kwargs):
        """ Do requests """
        if params is None:
            params = {}
        url = self._get_url(endpoint)
        auth = None
        headers = {
            "Accept": "application/json",
            "X-SECRET-KEY": self.secret,
            "X-API-KEY": self.public_key,
            "X-PRIVATE-KEY": self.private_key,
        }

        return request(
            method=method,
            url=url,
            verify=self.verify_ssl,
            auth=auth,
            params=params,
            data=data,
            timeout=self.timeout,
            headers=headers,
            **kwargs
        )

    def get(self, endpoint, **kwargs):
        """ Get requests """
        return self._request("GET", endpoint, None, **kwargs)

    def post(self, endpoint, data, **kwargs):
        """ POST requests """
        return self._request("POST", endpoint, data, **kwargs)

    def put(self, endpoint, data, **kwargs):
        """ PUT requests """
        return self._request("PUT", endpoint, data, **kwargs)

    def delete(self, endpoint, **kwargs):
        """ DELETE requests """
        return self._request("DELETE", endpoint, None, **kwargs)

    def options(self, endpoint, **kwargs):
        """ OPTIONS requests """
        return self._request("OPTIONS", endpoint, None, **kwargs)

    def verify_transaction(self, transaction_id):
        self.is_api = True
        data = {"transactionId": transaction_id}
        return self.post(endpoint='transactions/status', data=data)

    def refund_transaction(self, transaction_id):
        self.is_api = True
        data = {"transactionId": transaction_id}
        return self.post(endpoint='transactions/revert', data=data)

    def setup_payout(self, algorithm, destination, destination_type, roof_amount=None,
                     send_notification=True, rate_frequency=RATE_FREQUENCIES["1"], country_code="229"):
        data = {
            "destination": country_code + destination if destination_type == "1" else destination,
            "send_notification": 1 if send_notification else 0,
        }

        if destination_type not in DESTINATION_TYPES.keys():
            raise KKiapayDestinationTypeException()

        if algorithm not in ALGORITHMS.keys():
            raise KKiapayAlgorithmException()

        data["destination_type"] = DESTINATION_TYPES[destination_type]
        data['algorithm'] = ALGORITHMS[algorithm]

        if algorithm == "2":
            data["roof_amount"] = roof_amount if roof_amount else self.roof_amount
        else:
            if rate_frequency in RATE_FREQUENCIES.values():
                data["rate_frequency"] = rate_frequency
            else:
                data["rate_frequency"] = RATE_FREQUENCIES["1"]

        self.is_api = False
        return self.post("merchant/payouts/schedule", data=data)
