QUARTER_VALUE = 0.25
BONUS = 0.05
MIN_QUARTERS = 20
MAX_QUARTERS = 200
num_quarters = int(input("Number of quarters: "))
if num_quarters < MIN_QUARTERS or num_quarters > MAX_QUARTERS:
    print("Unable to accept that amount!")
else:
    quarter_val = num_quarters * QUARTER_VALUE
    bonus = quarter_val * BONUS
    total = quarter_val + bonus
    print("{} quarters = ${:.2f}".format(num_quarters, quarter_val))
    print("Bonus = ${:.2f}".format(bonus))
    print("Total depost = {:.2f}".format(total))