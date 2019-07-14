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
    def test_urls(self):
        live = Kkiapay("public_key", "private_key", "secret")
        sandbox = Kkiapay("public_key", "private_key", "secret", sandbox=True)

        assert live.url == Kkiapay.BASE_URL
        assert sandbox.url == Kkiapay.SANDBOX_URL

    def test_requests(self, requests_mock):
        pass
