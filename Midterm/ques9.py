def values_above_threshold(values, threshold):
    filtered = []
    i = 0
    while i < len(values):
        value = values[i]
        if value > threshold:
            filtered.append(value)
        i = i + 1
    return filtered
