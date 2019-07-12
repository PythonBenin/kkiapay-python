# kkiapay-python
> ⚠️ [Work In Progress] Community-driven admin KkiaPay Sdk for Python


## Introduction


## Installation

`kkiapay-python`

```bash
pip install kkiapay
```

## Usage

Behold, the power of `kkiapay-python`:

```python
from kkiapay import Kkiapay

k = Kkiapay('public_key', 'private_key', 'secret', sandbox=True)

transaction = k.verify_transaction('LVFNrK1nx')

print(transaction)
# => KkiapayTransaction(
#       performed_at='2019-07-11T11:24:42.687Z',
#       type='DEBIT',
#       status='FAILED',
#       source='MOBILE_MONEY',
#       amount=1,
#       fees=0,
#       country='BJ',
#       reason='invalid_number',
#       transactionId='LVFNrK1nx',
#       performedAt='07/11/2019'
#   )

print(transaction.status)
# => FAILED
```

## Roadmap

`kkiapay-python` is still under heavy development, we decided to ship it in this early stage so you can help us make it better.

Here's the plan for what's coming:
