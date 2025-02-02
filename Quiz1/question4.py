num = int(input("Enter an integer: "))
if num % 3 == 0:
    print(-num)
else:
    if num < 0:
      print(num ** 3)
    else:
      print(num)