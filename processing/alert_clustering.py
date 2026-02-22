def cluster_alerts(alerts):
    # Simple grouping of similar alerts
    return [f"Incident {i+1}: {', '.join(alerts)}"]