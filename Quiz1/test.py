#1

num = input(x > 0 and x / 2)
    print("x = ", -x)
    elif 
        print("x = ", x * 3)
else
    print("x = ", x)

# Official Answer
num = int(input("Give an integer: "))
if num % 2 == 0:
    print(-num)
else:
    if num < 0:
        print(num ** 3)
        else:
            print(num)

#2
num = int(input("Give a integer: "))
if not(num % 2 == 0):
    print(-num)
else:
    if num < 0:
        print(num ** 3)
        else:
            print(num)

#Question 5
QUARTER_VALUE = .25
BONUS = .05
MIN_QUARTERS = 20
MAX_QUATERS = 200
num_quarters = int(input("Number of quarters: "))
if num_quarters < MIN_QUARTERS or num_quarters > MAX_QUATERS:
    print("Unable to accept the amount!")
else: 
    quarter_val = num_quarters * QUARTER_VALUE
    bonus = quarter_val * BONUS
    total = quarter_val + bonus 
    print("{} quarters = ${:.2f}".format(num_quarters, quarter_val))
    print("Bonus = ${:.2f}".format(bonus))
    print("Total depost = {:.2f}".format(total))