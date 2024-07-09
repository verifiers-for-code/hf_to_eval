def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    

    Action Plan:
    1. Convert the input number `n` to a string `n_str` to access its digits easily.
    2. Initialize a variable `product` to store the product of the odd digits, set it to 1.
    3. Iterate through each character `digit` in `n_str`:
        a. Convert the character `digit` back to an integer using `int(digit)`.
        b. Check if the digit is odd by using the modulo operator (`%`): `digit % 2!= 0`.
        c. If the digit is odd, multiply the `product` by the digit.
    4. After iterating through all digits, return the final value of `product`.
        - If all digits are even, `product` will remain 1, so return 0.
        - If there are odd digits, `product` will hold their product, so return it."""
    
    n_str = str(n)
    product = 1
    for digit in n_str:
        digit_int = int(digit)
        if digit_int % 2 != 0:
            product *= digit_int
    return product if product != 1 else 0