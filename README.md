# Currency Converter Microservice (Text File Communication)

This microservice converts a currency amount in USD to a supported currency (`EUR`, `JPY`, `GBP`) using a simple text file as a communication pipe.

## Communication Contract

### How to Programmatically **Request** Data

1. Write a conversion request to `comm_pipe.txt`.  
2. Format:  
   ```
   <amount>,<from_currency>,<to_currency>
   ```

### Example (Python)
```python
with open("comm_pipe.txt", "w") as f:
    f.write("10,USD,EUR")
```

### How to Programmatically **Receive** Data

1. Read the result from `comm_pipe_response.txt`.
2. The service writes the converted result after 1–2 seconds.

### Example (Python)
```python
import time

time.sleep(2)  # wait for microservice to process

with open("comm_pipe_response.txt", "r") as f:
    result = f.read()

print("Converted result:", result)
```

### Example Output:
```
10.0 USD = 9.1 EUR (Rate: 0.91)
```

---

## UML Sequence Diagram 
```plaintext
Client Program            comm_pipe.txt             Currency Conversion Microservice
      |                         |                                   |
      |--- write: "10,USD,EUR" --->|                                 |
      |                         |--- read input ------------------->|
      |                         |<-- write result ------------------|
      |<-- read result ----------|                                   |
```

## Supported Currencies
- **From currency**: USD only
- **To currency options**:
  - EUR
  - GBP
  - JPY

## Input Validation
- The amount must be a valid number
- Only the listed currencies are supported
- Invalid or malformed input returns `"ERROR: Unsupported currency"` or similar
