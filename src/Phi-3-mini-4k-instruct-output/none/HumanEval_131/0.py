def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    all_even = True
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        else:
            all_even = False
        n //= 10
    return product if not all_even else 0