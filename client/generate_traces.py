import json, random, time

def generate_traces():
    return {
        "Service": f"Service-{random.randint(1,5)}",
        "Trace ID": random.randint(1000,9999),
        "Latency(ms)": random.randint(50, 500),
        "Error": random.choice([True, False])
    }

if __name__ == "__main__":
    while True:
        traces = generate_traces()
        with open("../dashboard/mock_data.json", "a") as f:
            f.write(json.dumps(traces) + "\n")
        print("Generated Trace:", traces)
        time.sleep(3)