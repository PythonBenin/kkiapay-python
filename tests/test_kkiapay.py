

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
        live = Kkiapay('public_key', 'private_key', 'secret')
        sandbox = Kkiapay('public_key', 'private_key', 'secret', sandbox=True)

        assert live.url == Kkiapay.BASE_URL
        assert sandbox.url == Kkiapay.SANDBOX_URL


    def test_answer(self, requests_mock):
        pass
        # requests_mock.get("http://123-fake-api.com", text="Hello!")
        # requests_mock.get("http://123-fake-api.com", text="Hello!")
        # response = requests.get("http://123-fake-api.com")

        # assert response.text == "Hello!"



    # k = Kkiapay('a1fc2c00410911e991519dc1901933da', 'pk_a1fc5310410911e991519dc1901933da', 'sk_a1fc5311410911e991519dc1901933da')

    # r = k.verify_transaction('qM0enu1Czb')