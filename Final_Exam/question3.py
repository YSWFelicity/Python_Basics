def spam(n):
    if n <= 1:
        return 0
    else:
        return 1 + spam(n // 2)

   
def main():
    print(spam(-1))


if __name__ == '__main__':
    main()
