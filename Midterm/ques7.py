def sum_even(nums):
    if len(nums) == 0:
        return 0
    else:
        if nums[0] % 2 == 0:
            return nums[0] + sum_even(nums[1:])
        else:
            return sum_even(nums[1:])


def main():
    print("nums = [1, 2, 3, 4]")


if __name__ == "__main__":
    main()
