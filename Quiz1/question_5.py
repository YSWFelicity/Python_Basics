'''
This is separated into 4 blocks.
Each block corresponds to a possible question variant.
'''


# Variant 1 -------------------------------------------------------------------
'''
- The amount in dollars of their deposit before the 5% bonus.
- The bonus amount in dollars.
- The total amount deposited, including the bonus.
- All three amounts should be formatted to 2 decimal places.
'''
QUARTER_VALUE = .25
BONUS = .05
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

num_quarters = int(input("Number of quartersL "))
if num_quarters < MIN_QUARTERS or num_quarters > MAX_QUARTERS:
    print("Unable to accept that amount!")
else: 
    quarter_val = num_quarters * QUARTER_VALUE
    bonus = quarter_val * BONUS 
    total = quarter_val + bonus 
    print("Number of quarters")
QUARTER_VALUE = 0.25
BONUS = 0.05
MIN_QUARTERS = 20
MAX_QUARTERS = 200


# Variant 2 -------------------------------------------------------------------
'''
- The amount that the user wants to convert in CAD
- The amount converted to USD
- The fee in USD
'''
CAD_TO_USD = 1.34
FEE = .03
MIN_CAD = 50
MAX_CAD = 1000
amount_cad = int(input("Amount to convert in CAD: "))
if amount_cad < MIN_CAD or amount_cad > MAX_CAD:
    print("Unable to convert that amount!")
else:
    amount_usd = amount_cad / CAD_TO_USD
    fee = FEE * amount_usd
    print("{:.2f} CAD is {:.2f} USD".format(amount_cad, amount_usd))
    print("Fee: {:.2f} USD".format(fee))

# Variant 3 -------------------------------------------------------------------
'''
- The amount that the user wants to convert in USD
- The amount converted to GBP
- The fee in USD
'''
GBP_TO_USD = .78
FEE = .05
MIN_USD = 100
MAX_USD = 5000
amount_usd = int(input("Amount to convert in USD: "))
if amount_usd < MIN_USD or amount_usd > MAX_USD:
    print("Unable to convert that amount!")
else:
    amount_gbp = amount_usd * GBP_TO_USD
    fee = FEE * amount_usd
    print("{:.2f} USD is {:.2f} GBP".format(amount_usd, amount_gbp))
    print("Fee: {:.2f} USD".format(fee))
# Variant 4 -------------------------------------------------------------------
'''
- The amount requested in dollars, before the 2% fee is added.
- The fee amount in dollars.
- The total amount the customer needs to give the bank, including the fee.
'''
QUARTER_VALUE = .25
FEE = .02
MIN_QUARTERS = 20
MAX_QUARTERS = 100
num_quarters = int(input("Number of quarters needed: "))
if num_quarters < MIN_QUARTERS or num_quarters > MAX_QUARTERS:
    print("Unable to provied that amount!")
else:
    quarter_val = num_quarters * QUARTER_VALUE
    fee = quarter_val * FEE
    total = quarter_val + fee
    print("{} quarters = ${:.2f}".format(num_quarters, quarter_val))
    print("Fee = ${:.2f}".format(fee))
    print("Amount owed = {:.2f}".format(total))