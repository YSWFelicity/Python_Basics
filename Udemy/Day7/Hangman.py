import random

word_list = ["aardvark", "baboon", "camel"]

guess_word = random.choice(word_list)
print(guess_word)

guess_letter = input("Guess a word: ").lower()

for letter in guess_word:
    if guess_letter == letter:
        print("Right")
    else:
        print("Wrong")
