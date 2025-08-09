Currency Converter Microservice
This microservice converts amounts from USD to supported currencies (EUR, JPY, GBP) and serves a simple HTML interface with a dropdown menu for currency selection.
---
Features
- Convert USD to Euro (EUR), Japanese Yen (JPY), British Pound (GBP)
- Input validation (must be numeric and non-negative)
- REST API for integration with other programs
- HTML frontend with dropdown currency selection populated from /rates
- JSON-based responses
---
Endpoints
GET /
Serves the HTML frontend (index.html).
GET /rates
Returns the list of supported currencies, their exchange rates, and human-readable labels.
POST /convert
Converts an amount from USD to the selected currency.
---
Example Programmatic Call (Python)
import requests# Get ratesrates = requests.get("http://127.0.0.1:5000/rates").json()print(rates)# Convert 10 USD to EURpayload = {"amount": 10, "from_currency": "USD", "to_currency": "EUR"}result = requests.post("http://127.0.0.1:5000/convert", json=payload).json()print(result)
---
UML Sequence Diagram
Flow:
1) Frontend calls GET /rates to populate the dropdown.
2) User selects a currency and submits.
3) Frontend calls POST /convert with amount, from_currency, and to_currency.
4) Service returns either 200 with converted result or 400 with an error.
[![](https://img.plantuml.biz/plantuml/svg/TP5BQyCm48Jl-XL33YK6nqqVfnnAm3Gzjf3s75HvGqLaAQnaqnBytolvKLgQ77Ttvfk1NViWEJIr4L85ntZpnE8OLrhfexG1imqx6yXMc6jRqMVn4MgJpI0z-ijVSTamarLVA9rjYGCnjiIjLeJvnaX_69pZJeWKXyN3W5hXDeidGof0JQ0ha4qOMRicflN2v1WHAznaU7fynJNBG5vCQOjVqEKIf_wQmyXtChxx5rmQhGvJwJCXTnbUdhSnHGqId8O-EVRiwjtKDaTmFqDtiSm8eMetKLAz74LHd3NT9nCnE-xY5_RGjfL6LvbOnx-attq3)](https://editor.plantuml.com/uml/TP5BQyCm48Jl-XL33YK6nqqVfnnAm3Gzjf3s75HvGqLaAQnaqnBytolvKLgQ77Ttvfk1NViWEJIr4L85ntZpnE8OLrhfexG1imqx6yXMc6jRqMVn4MgJpI0z-ijVSTamarLVA9rjYGCnjiIjLeJvnaX_69pZJeWKXyN3W5hXDeidGof0JQ0ha4qOMRicflN2v1WHAznaU7fynJNBG5vCQOjVqEKIf_wQmyXtChxx5rmQhGvJwJCXTnbUdhSnHGqId8O-EVRiwjtKDaTmFqDtiSm8eMetKLAz74LHd3NT9nCnE-xY5_RGjfL6LvbOnx-attq3)
---
Communication Contract
- Protocol: HTTP
- Request Format: JSON for /convert
- Response Format: JSON
- Validation: amount must be a positive number; from_currency must be USD; to_currency must be one of: EUR, JPY, GBP.
---
Running Locally
1. Install dependencies:   pip install flask requests
2. Run the app:   python3 currency_converter.py
3. Open the UI:   http://127.0.0.1:5000/
