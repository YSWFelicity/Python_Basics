def add_tip(bill_amt, percentage):
    MIN_TIP = 0.1
    MAX_TIP = 1
    if percentage < MIN_TIP:
        raise ValueError("Tip must be at least 0.1 (10%)")
    if percentage > MAX_TIP:
        raise ValueError("Tip must be a float between 0.1 (10%) and 1 (100%)")
    return bill_amt + bill_amt * percentage
