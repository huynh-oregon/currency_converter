from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/favicon.ico")
def favicon():
    return ("", 204)


# Hardcoded exchange rates from USD
EXCHANGE_RATES = {
    "EUR": 0.91,
    "JPY": 145.32,
    "GBP": 0.78
}
CURRENCY_LABELS = {
    "EUR": "Euro",
    "JPY": "Japanese Yen",
    "GBP": "British Pound"
}

@app.route("/rates", methods=["GET"])
def rates():
    # used by the UI to populate the dropdown
    return jsonify({"base": "USD", "rates": EXCHANGE_RATES, "labels": CURRENCY_LABELS}), 200

@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.get_json(force=True)

        # Validate amount
        amount = data.get("amount")
        if amount is None or not isinstance(amount, (int, float, str)):
            return jsonify({"error": "Invalid input. 'amount' must be a number."}), 400

        try:
            amount = float(amount)
        except ValueError:
            return jsonify({"error": "Invalid input. 'amount' must be a number."}), 400

        if amount < 0:
            return jsonify({"error": "Invalid input. 'amount' must be a positive number."}), 400

        from_currency = data.get("from_currency", "USD").upper()
        to_currency = data.get("to_currency", "").upper()

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
        }), 200

    except (TypeError, KeyError):
        return jsonify({"error": "Invalid input. Expect JSON: {amount, from_currency, to_currency}"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
