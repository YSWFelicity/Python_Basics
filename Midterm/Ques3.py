def validator(message, option):
    if len(message) == 0 or option < 0 or option > 2:
        return "Invalid"
    if option == 0:
        if len(message) >= 3:
            return message[-3:]
        return message[-1]
    elif option == 1:
        if len(message) >= 3:
            return message[:3]
        return message[0]
    else:
        if len(message) % 2 == 0:
            return message.upper()
        return message.lower()


def main():
    print(validator("Roses are red", 1))
    print(validator("Hi", 0))
    print(validator("Hello", 3))
    print(validator("AB", 1))
    print(validator("Friday", 2))


if __name__ == "__main__":
    main()
