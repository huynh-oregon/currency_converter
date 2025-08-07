import requests

data = {
    "amount": 10.00,
    "from_currency": "USD",
    "to_currency": "EUR"
}

response = requests.post("http://localhost:5000/convert", json=data)

if response.ok:
    print("Response JSON:")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.json())
