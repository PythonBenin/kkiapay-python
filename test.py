from kkiapay import Kkiapay

k = Kkiapay('b348e580a3c311e98ffb7b8677e53978', 'tpk_b3490c91a3c311e98ffb7b8677e53978', 'tsk_b3490c92a3c311e98ffb7b8677e53978', sandbox=True)

transaction = k.verify_transaction('LVFNrK1nx')

print(transaction.status)

transaction2 = k.refund_transaction('LVFNrK1nx')

print(transaction2)