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

print(transaction.status)
# => FAILED
```

## Roadmap

`kkiapay-python` is still under heavy development, we decided to ship it in this early stage so you can help us make it better.

Here's the plan for what's coming:
