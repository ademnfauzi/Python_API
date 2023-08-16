import requests
import time
import psutil

# Define the API endpoint
url = "https://randomuser.me/api/"

# Define the number of requests to make
num_requests = 10

# Define the expected response code
expected_response_code = 200

# Define the headers and payload (if needed)
headers = {'Content-Type': 'application/json'}
payload = {}

# Measure the performance metrics for each request
for i in range(num_requests):
    # Start the timer
    start_time = time.time()

    # Make the request
    response = requests.get(url, headers=headers, json=payload)

    # Calculate the latency in milliseconds
    latency_ms = (time.time() - start_time) * 1000

    # Get the response code
    response_code = response.status_code

    # Get the response size in bytes
    response_size_bytes = len(response.content)

    # Print the performance metrics
    print(f"Request {i+1} - Latency: {latency_ms:.2f} ms, Response Code: {response_code}, Response Size: {response_size_bytes} bytes")

    # Wait for a short time between requests to simulate a realistic load
    time.sleep(0.1)

# Calculate the average load time
avg_load_time = psutil.cpu_percent(interval=1) / 100 * num_requests

# Print the average load time

print(response.json())

print(f"Average Load Time: {avg_load_time:.2f} s")
