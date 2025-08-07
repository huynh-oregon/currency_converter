from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded exchange rates
EXCHANGE_RATES = {
    "EUR": 0.91,
    "JPY": 145.32,
    "GBP": 0.78
}

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()

    try:
        amount = float(data["amount"])
        from_currency = data["from_currency"]
        to_currency = data["to_currency"]

        if from_currency != "USD" or to_currency not in EXCHANGE_RATES:
            return jsonify({"error": "Unsupported currency"}), 400

        rate = EXCHANGE_RATES[to_currency]
        converted = round(amount * rate, 2)

        return jsonify({
            "original_amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": converted,
            "rate": rate
        })

    except (ValueError, KeyError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
