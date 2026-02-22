def cluster_alerts(cpu, memory, errors):
    if cpu > 80 and memory > 75 and errors > 5:
        return "Critical: Possible system overload condition detected."
    elif cpu > 80 or memory > 75:
        return "Warning: Resource utilization is high."
    else:
        return "System operating within normal parameters."