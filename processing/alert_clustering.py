# processing/alert_clustering.py

def cluster_alerts(metrics):
    """
    Simple alert clustering based on metrics.
    Returns a list of alert strings.
    """
    alerts = []

    if metrics.get("CPU Usage", 0) > 80:
        alerts.append("High CPU Usage")

    if metrics.get("Memory Usage", 0) > 80:
        alerts.append("High Memory Usage")

    if metrics.get("Errors", 0) > 5:
        alerts.append("Multiple Errors")

    if metrics.get("Response Time(ms)", 0) > 800:
        alerts.append("Slow Response Time")

    # Return a formatted list of incidents
    if alerts:
        # Use enumerate to create incident numbers
        return [f"Incident {idx+1}: {alert}" for idx, alert in enumerate(alerts)]
    else:
        return []