# processing/timeline_narrator.py

def narrate_timeline(metrics):
    """
    Generate a human-readable incident timeline
    based on metrics. Returns a string.
    """
    timeline = []

    if metrics.get("Errors", 0) > 5:
        timeline.append("Multiple errors detected! Investigate immediately.")
    else:
        timeline.append("System running smoothly.")

    if metrics.get("CPU Usage", 0) > 80:
        timeline.append("High CPU usage observed.")

    if metrics.get("Memory Usage", 0) > 80:
        timeline.append("High Memory usage observed.")

    if metrics.get("Response Time(ms)", 0) > 800:
        timeline.append("Response time is slower than usual.")

    return "\n".join(timeline)