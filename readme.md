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
- [x] Refund Transaction - `Only available on Live`
- [x] Schedule Payout
- [ ] Add better errors and exceptions handling
- [ ] Add tests.


## Schedule Payout

### Example
Below is an example of the function usage:
```python
# Setup Scheduled Payout using 'ROOF' algorithm
schedule_payout = k.setup_payout(algorithm = '2',
                                 roof_amount = '10000',
                                 destination = '61000000',
                                 destination_type = '1',
                                 send_notification = True,
                                 country_code = '229'
                                )

print(schedule_payout)
#{
#	'response': 
#	{
#		'merchant': '5d34445784deb700073a0281', 
#		'meta_data': '', 
#		'algorithm': 'roof', 
#		'rate_frequency': '', 
#		'roof_amount': '10000', 
#		'active': True, 
#		'send_notification': True, 
#		'destination_type': 'MOBILE_MONEY', 
#		'destination': '22961000000', 
#		'job_name': '', 
#		'account': '5d34445784deb700073a0282'
#	}, 
#	'status_code': 200
#}
```

### Attribute Matrix
|        Name       | Required |               Possible Values              |                                    Description                                    |
|:-----------------:|:--------:|:------------------------------------------:|:---------------------------------------------------------------------------------:|
|     **algorithm**     |     **M**    |         {"1": 'rate', "2": 'roof'}         |                         Specify the algorithm to be used.                         |
|  **destination_type** |     **M**    | {"1": 'MOBILE_MONEY', "2": 'BANK_ACCOUNT'} |                            Specify the Destination type                           |
|    **destination**    |     **M**    |                 '61000000'                 |                              Specify the Destination number/account Number                                                     |
|   **rate_frequency**  |    M/O   	|      {"1": '3d', "2": '1w', "3": '1m'}     |       Specify the Rate Frequency. Required in case 'rate' algorithm is used       |
|    **roof_amount**    |    M/O   |                   '10000'                  |                              Specify the Roof amount.                             |
| **send_notification** |     O    |            Boolean (True, False)           |                      Specify is a Notification should be sent                     |
|    **country_code**   |     O    |                    '229'                   | Specify the Country Code of the destination number is case 'MOBILE MONEY' is used |


## Contributing

Check our [contribution guide](CONTRIBUTING.md).

## License

`kkiapay-python` is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
