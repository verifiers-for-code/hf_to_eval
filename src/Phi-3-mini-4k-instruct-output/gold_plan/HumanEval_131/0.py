def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15

    Action Plan:
    1. Initialize variables to store the product of odd digits and count of odd digits.
    2. Convert the input number to a string to iterate through its digits.
    3. For each digit in the number:
       a. Convert the digit back to an integer.
       b. Check if the digit is odd (hint: use modulo operator).
       c. If odd, multiply it with the product and increment the odd count.
    4. After the loop, check if any odd digits were found:
       a. If no odd digits (count is 0), return 0.
       b. Otherwise, return the calculated product.
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 1:
            product *= digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product