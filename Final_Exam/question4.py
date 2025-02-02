def main():
    plant_seasion = {
        "blueberry": "fall or spring",
        "tomato": "spring",
        "pumpkin": "late spring",
        "cabbage": "spring or late summer",
        "strawberry": "early spring"
    }
    while True:
        user_input = input("Enter a plant name: ")
        user_input = user_input.lower()
        if user_input == "q":
            break
        if user_input in plant_seasion:
            print(plant_seasion[user_input])
        else:
            print("I don't know when to plant " + user_input)


if __name__ == "__main__":
    main()
