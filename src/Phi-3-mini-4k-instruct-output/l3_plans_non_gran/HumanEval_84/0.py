def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    

    Action Plan:
    1. Define a function `solve` that takes a positive integer `N` as input.
    2. Convert the input integer `N` to a binary string using the `bin()` function.
    3. Remove the '0b' prefix from the binary string using string slicing.
    4. Convert the binary string to a list of digits using the `list()` function.
    5. Calculate the sum of the digits in the list using the `sum()` function.
    6. Convert the sum to a binary string using the `bin()` function again.
    7. Remove the '0b' prefix from the binary string of the sum.
    8. Return the final binary string as the output.
    
    Note: Ensure the function handles the constraints specified (0 ≤ N ≤ 10000)."""
    if N < 0 or N > 10000:
        raise ValueError("Input must be a positive integer between 0 and 10000.")
    
    binary_str = bin(N)[2:]
    digit_list = list(binary_str)
    digit_sum = sum(int(digit) for digit in digit_list)
    result = bin(digit_sum)[2:]
    
    return result