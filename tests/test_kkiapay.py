

from .context import kkiapay
from kkiapay import Kkiapay

def test_answer():
    k = Kkiapay('a1fc2c00410911e991519dc1901933da', 'pk_a1fc5310410911e991519dc1901933da', 'sk_a1fc5311410911e991519dc1901933da')

    r = k.verify_transaction('qM0enu1Czb')