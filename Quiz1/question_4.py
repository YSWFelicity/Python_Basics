'''
This is separated into 4 blocks.
Each block corresponds to a possible question variant.
They are all basically the same except for the first conditional
'''


# Variant 1 -------------------------------------------------------------------
'''
- If the integer is positive and divisible by 2, convert it to its negative
  equivalent and print the result.
- Otherwise, if the integer is negative and NOT divisible by 2, cube the
  number and print the result.
- If neither of the above apply, print the number as is.
'''
num = int(input("Give an integer: "))
if num % 2 == 0:
    print(-num)
else:
    if num < 0:
        print(num ** 3)
    else:
        print(num)
# Variant 2 -------------------------------------------------------------------
'''
- If the integer is positive and NOT divisible by 2, convert it to  its
  negative equivalent and print the result.
- Otherwise, if the integer is negative and divisible by 2, cube the number
  and print the result.
- If neither of the above apply, print the number as is.
'''
num = int(input("Give an integer: "))
if not(num % 2 == 0):
    print(-num)
else:
    if num < 0:
        print(num ** 3)
    else:
        print(num)
# Variant 3 -------------------------------------------------------------------
'''
- If the integer is positive and NOT divisible by 5, convert it to  its
  negative equivalent and print the result.
- Otherwise, if the integer is negative and divisible by 5,  cube the number
  and print the result.
- If neither of the above apply, print the number as is.
'''
num = int(input("Give an integer: "))
if not(num % 5 == 0):
    print(-num)
else:
    if num < 0:
        print(num ** 3)
    else:
        print(num)

# Variant 4 -------------------------------------------------------------------
'''
- If the integer is positive and divisible by 3, convert it to its
  negative equivalent and print the result.
- Otherwise, if the integer is negative and NOT divisible by 3,  cube the number
  and print the result.
- If neither of the above apply, print the number as is.
'''
num = int(input("Give an integer: "))
if num % 3 == 0:
    print(-num)
else:
    if num < 0:
        print(num ** 3)
    else:
        print(num)

num = int(input("The integer is: "))
if num % 3 == 0:
    print(-num)
else:
    if num < 0:
      print(num ** 3)
    else:
      print(num)