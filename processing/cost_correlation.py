# processing/cost_correlation.py

def correlate_cost(metrics):
    """
    Simulate cost-performance correlation.
    Returns estimated cost impact in dollars.
    """
    # Simple mock calculation for demo
    base_cost = 1000
    cpu_factor = metrics.get("CPU Usage", 0) * 2
    memory_factor = metrics.get("Memory Usage", 0) * 1.5
    error_factor = metrics.get("Errors", 0) * 50

    estimated_cost = base_cost + cpu_factor + memory_factor + error_factor
    return estimated_cost