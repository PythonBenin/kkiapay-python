import requests

url = "https://api.kkiapay.me/api/v1/transactions/status"

payload = {'transactionId': 'qM0enu1Czb'}
headers = {
    'Accept': "application/json",
    'X-API-KEY': "a1fc2c00410911e991519dc1901933da",
    'X-PRIVATE-KEY': "pk_a1fc5310410911e991519dc1901933da",
    'X-SECRET-KEY': "sk_a1fc5311410911e991519dc1901933da",
    }

response = requests.post(url, data=payload, headers=headers)

print(response.text)