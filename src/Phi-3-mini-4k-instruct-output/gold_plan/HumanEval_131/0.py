def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Step 1: Initialize variables to store the product of odd digits and count of odd digits.
    product = 1
    odd_count = 0

    # Step 2: Convert the input number to a string to iterate through its digits.
    n_str = str(n)

    # Step 3: For each digit in the number
    for digit in n_str:
        # a. Convert the digit back to an integer.
        digit_int = int(digit)

        # b. Check if the digit is odd (hint: use modulo operator).
        if digit_int % 2 != 0:
            # c. If odd, multiply it with the product and increment the odd count.
            product *= digit_int
            odd_count += 1

    # Step 4: After the loop, check if any odd digits were found
    if odd_count == 0:
        # a. If no odd digits (count is 0), return 0.
        return 0
    # b. Otherwise, return the calculated product.
    return product