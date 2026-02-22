import json, random, time

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
        with open("../dashboard/mock_data.json", "w") as f:
            json.dump(metrics, f)
        print("Generated Metrics:", metrics)
        time.sleep(3)