print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
split = (total_bill * (1+tip/100)) / people
print(f"Each person should pay: ${split}")