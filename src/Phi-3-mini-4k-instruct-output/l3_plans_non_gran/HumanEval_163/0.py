def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    

    Action Plan:
    1. Define a function `generate_integers` that takes two positive integers `a` and `b` as input.
    2. Initialize an empty list `even_digits` to store the even digits.
    3. Iterate through the range of numbers from `a` to `b` (inclusive) using a loop.
    4. For each number in the range:
        a. Check if the number is even by using the modulo operator (`%`).
        b. If the number is even, convert it to a string and check if all its digits are even.
        c. If both conditions are met, add the original number to the `even_digits` list.
    5. After the loop, return the `even_digits` list.
    6. Test the function with example inputs to ensure it produces the correct output.
    """
    even_digits = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            digits = [int(digit) for digit in str(num)]
            if all(digit % 2 == 0 for digit in digits):
                even_digits.append(num)
    return even_digits