print("Welcome to the rollarcoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You can ride the rollarcoaster!")
  age = int(input("What is your age?"))
  if age <= 12:
    bill = 5
    print("You need to pay $5")
  elif age <= 18:
    bill = 7
    print("You need to pay $7")
  elif 45 <= age <= 55:
    print("Have a free ride on us!")
  else:
    bill = 12
    print("You need to pay $12")
  
  photo = input("Do you want a photo? Y for yes and N for no: ")
  if photo == 'Y':
    bill += 3
  
  print(f"Your final bill is ${bill}")

else: 
  print("Sorry you cannot.")