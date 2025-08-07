import time

# Write request to pipe
with open("comm_pipe.txt", "w") as f:
    f.write("10,USD,EUR")

# Wait for microservice to process
print("Request sent. Waiting for response...")
time.sleep(2)

# Read response from output pipe
with open("comm_pipe_response.txt", "r") as f:
    result = f.read()

print("Received response:", result)
