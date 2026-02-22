def generate_explanation(cpu, memory, errors):
    if cpu > 80 and errors > 5:
        return "High CPU usage combined with rising error logs suggests possible service overload or inefficient processing."
    elif memory > 75:
        return "Elevated memory usage indicates potential memory leak or heavy workload."
    else:
        return "System metrics are stable with no immediate risk detected."