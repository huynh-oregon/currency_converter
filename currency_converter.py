import time

EXCHANGE_RATES = {
    "EUR": 0.91,
    "JPY": 145.32,
    "GBP": 0.78
}

def read_input():
    try:
        with open("comm_pipe.txt", "r") as f:
            content = f.read().strip()
            if content:
                parts = content.split(",")
                if len(parts) != 3:
                    return None
                amount = float(parts[0])
                from_currency = parts[1]
                to_currency = parts[2]
                return amount, from_currency, to_currency
    except:
        return None
    return None

def write_output(response):
    with open("comm_pipe_response.txt", "w") as f:
        f.write(response)

def convert(amount, from_currency, to_currency):
    if from_currency != "USD" or to_currency not in EXCHANGE_RATES:
        return "ERROR: Unsupported currency"
    rate = EXCHANGE_RATES[to_currency]
    converted = round(amount * rate, 2)
    return f"{amount} {from_currency} = {converted} {to_currency} (Rate: {rate})"

if __name__ == "__main__":
    print("Currency converter (text file pipeline) running...")
    last_request = ""
    while True:
        data = read_input()
        if data:
            amount, from_currency, to_currency = data
            request_string = f"{amount},{from_currency},{to_currency}"
            if request_string != last_request:
                result = convert(amount, from_currency, to_currency)
                write_output(result)
                print("Processed:", result)
                last_request = request_string
        time.sleep(1)
