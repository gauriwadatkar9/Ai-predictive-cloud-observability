def calculate_risk(cpu, memory, errors):
    score = 100 - (cpu*0.3 + memory*0.3 + errors*4)
    return max(0, round(score))