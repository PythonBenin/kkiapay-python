# kkiapay-python

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
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

### Verify a transaction

```python
from kkiapay import Kkiapay

k = Kkiapay('public_key', 'private_key', 'secret', sandbox=True)

transaction = k.verify_transaction('LVFNrK1nx')

print(transaction)
# => {
#    "performed_at":"2023-02-20T17:44:47.842Z",
#    "received_at":1676915100302,
#    "type":"DEBIT",
#    "status":"SUCCESS",
#    "source":"MOBILE_MONEY",
#    "source_common_name":"mtn-benin",
#    "amount":100,
#    "fees":2,
#    "net":0,
#    "externalTransactionId":"test",
#    "transactionId":"123",
#    ...
# }
```

### Refund a transaction

```python
from kkiapay import Kkiapay

k = Kkiapay('public_key', 'private_key', 'secret', sandbox=True)

transaction = k.refund_transaction('LVFNrK1nx')

print(transaction)
# => {
#    "code":"SUCCESS",
#    "description":"REVERTED",
#    "transactionId":"123"
# }
```

### Schedule Payout

Schedule payout API is deprecated and no longer supported as of Feb 20th, 2023 from the API and can be done only on the [dashboard](https://app.kkiapay.me/dashboard) until further notice.

## Contributing

Check our [contribution guide](CONTRIBUTING.md).

## License

`kkiapay-python` is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
