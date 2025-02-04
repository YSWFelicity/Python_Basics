print("Welcome to Treasure island. Your mission is to find the treasure.")

#加lower()这里是为了统一表达，所有的都是小写
output1 = input("left or right? Left or Right").lower()
if output1 == "left":
  output2 = input("Swim or Wait?").lower()
  if output2 == "swim":
    print("Game over.")
  elif output2 == "wait":
    output3 = input("Which door?").lower()
    if output3 == "red":
      print("Game over.")
    elif output3 == "blue":
      print("Game over.")
    elif output3 == "yellow":
      print("You win!")
    else:
      print("Game over.")
  else:
    print("Game over.")
elif output1 == "right":
  print("Game over.")
else:
  print("Game over.")

