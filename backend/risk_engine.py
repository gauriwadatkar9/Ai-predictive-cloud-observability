def calculate_risk(cpu, memory, errors):
    risk = 0

    if cpu > 80:
        risk += 30
    if memory > 75:
        risk += 25
    if errors > 5:
        risk += 30
    if cpu > 90 and memory > 85:
        risk += 15

    return min(risk, 100)