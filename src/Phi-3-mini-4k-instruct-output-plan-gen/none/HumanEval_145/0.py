
def order_by_points(nums):
    # Helper function to calculate the sum of digits of a number
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    # Sort the list using a custom key function
    nums.sort(key=lambda x: (sum_of_digits(x), nums.index(x)))
    return nums