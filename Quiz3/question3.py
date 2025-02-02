def sum_fives(n):
    if n % 5 != 0:
        return 0
    elif n == 0:
        return 0
    else:
        return n + sum_fives(n - 5)

print(sum_fives(1))