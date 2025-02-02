def valid_input(user_in):
    try:
        num = int(user_in)
    except ValueError:
        print('Exception: input is not an integer value')
        return False
    except IndexError:
        print("Invalid index. Try again.")
    return num % 10 == 0


def main():
    PROMPT = "Enter an integer that is divisible by 10: "
    num = input(PROMPT)
    while not valid_input(num):
        num = input(PROMPT)
    print("Done")


if __name__ == '__main__':
    main()
