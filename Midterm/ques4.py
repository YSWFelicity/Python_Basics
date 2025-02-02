def get_ticket_cost(group_ages):
    admissionRate = 20
    total = 0
    for i in group_ages:
        if i < 15:
            total = total + (admissionRate * 50) / 100
            i = i + 1
        elif i >= 60:
            total = total + (admissionRate * 25) / 100
        else:
            total = total + admissionRate
    return total
