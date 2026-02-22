import json, random, time
import os

# Get absolute path to mock_data.json
current_dir = os.path.dirname(os.path.abspath(__file__))  # client/
mock_file = os.path.join(current_dir, "..", "dashboard", "mock_data.json")
mock_file = os.path.abspath(mock_file)  # full absolute path

# Ensure folder exists
os.makedirs(os.path.dirname(mock_file), exist_ok=True)

def generate_metrics():
    return {
        "CPU Usage": random.randint(20, 90),
        "Memory Usage": random.randint(30, 95),
        "Errors": random.randint(0, 10),
        "Response Time(ms)": random.randint(100, 1000)
    }

if __name__ == "__main__":
    while True:
        metrics = generate_metrics()
        with open(mock_file, "w") as f:
            json.dump(metrics, f)
        print("Generated Metrics:", metrics)
        time.sleep(3)