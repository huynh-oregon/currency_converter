import time
import requests

BASE = "http://127.0.0.1:5000"

def convert_once(amount, to):
    start = time.perf_counter()
    r = requests.post(f"{BASE}/convert", json={
        "amount": amount,
        "from_currency": "USD",
        "to_currency": to
    })
    elapsed_ms = int((time.perf_counter() - start) * 1000)
    return r.status_code, r.json(), elapsed_ms

def main():
    # Happy path
    for target in ("EUR", "JPY", "GBP"):
        code, body, ms = convert_once(10.0, target)
        print(target, code, body, f"{ms} ms")
        assert code == 200, f"Expected 200, got {code}"
        assert body.get("to_currency") == target
        assert body.get("elapsed_ms", ms) <= 500, "Response exceeded 500 ms"

    # Negative amount
    code, body, ms = convert_once(-5, "EUR")
    print("NEG", code, body, f"{ms} ms")
    assert code == 400 and "positive number" in body.get("error", "")

    # Non-numeric amount
    r = requests.post(f"{BASE}/convert", json={
        "amount": "abc",
        "from_currency": "USD",
        "to_currency": "EUR"
    })
    print("NONNUM", r.status_code, r.json())
    assert r.status_code == 400 and "must be a number" in r.json().get("error", "")

    # Unsupported currency
    code, body, ms = convert_once(10, "XXX")
    print("UNSUP", code, body, f"{ms} ms")
    assert code == 400 and "Unsupported currency" in body.get("error", "")

    print("All checks passed.")

if __name__ == "__main__":
    main()
