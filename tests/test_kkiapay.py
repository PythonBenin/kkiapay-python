from .context import kkiapay
from kkiapay import Kkiapay
import requests_mock, requests


def setup_module(module):
    """ setup any state specific to the execution of the given module."""


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """


class TestKkiapay(object):
    live = Kkiapay("public_key", "private_key", "secret")
    sandbox = Kkiapay("public_key", "private_key", "secret", sandbox=True)

    def test_urls(self):
        assert self.live.url == Kkiapay.BASE_URL
        assert self.sandbox.url == Kkiapay.SANDBOX_URL

    def test_requests(self, requests_mock):
        pass

    def test_setup_payout(self, monkeypatch):
        results = {
            'response': {
                'merchant': '5d34445784deb700073a0281',
                'meta_data': '',
                'algorithm': 'roof',
                'rate_frequency': '',
                'roof_amount': '50000',
                'active': True,
                'send_notification': True,
                'destination_type': 'MOBILE_MONEY',
                'destination': '22961000000',
                'job_name': '',
                'account': '5d34445784deb700073a0282'
            },
            'status_code': 200}

        class MockJsonResponse:
            status_code = 200

            @staticmethod
            def json():
                return {
                    'merchant': '5d34445784deb700073a0281',
                    'meta_data': '',
                    'algorithm': 'roof',
                    'rate_frequency': '',
                    'roof_amount': '50000',
                    'active': True,
                    'send_notification': True,
                    'destination_type': 'MOBILE_MONEY',
                    'destination': '22961000000',
                    'job_name': '',
                    'account': '5d34445784deb700073a0282'
                }

        def kkiapay_api_mock_return(*args, **kwargs):
            return MockJsonResponse()

        monkeypatch.setattr(requests, 'post', kkiapay_api_mock_return)
        assert self.sandbox.setup_payout(algorithm="2", destination="61000000", destination_type="1") == results
        assert self.live.setup_payout(algorithm="1", destination="61000000", destination_type="1") == results
