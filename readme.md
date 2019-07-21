# kkiapay-python

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Road map](#road-map)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Community-driven admin KkiaPay Sdk for Python.

## Installation

To get the latest version of KkiaPay Sdk for Python , simply run:

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
print(transaction.amount)
# => 1
```

## Road map

`kkiapay-python` is still under heavy development, we decided to ship it in this early stage so you can help us make it better.

Here's the plan for what's coming:

- [x] Sandbox and Live environments
- [x] Verify Transaction
- [x] Refund Transaction
- [ ] Schedule Payout
- [ ] Add better errors and exceptions handling
- [ ] Add tests.

## Contributing

Check our [contribution guide](CONTRIBUTING.md).

## License

`kkiapay-python` is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
