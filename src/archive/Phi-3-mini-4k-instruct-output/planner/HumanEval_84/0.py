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
    1. Convert the input number N to a string to easily access its digits.
    2. Initialize a variable to store the sum of digits.
    3. Iterate through each character (digit) in the string representation of N:
        a. Convert the character to an integer.
        b. Add the integer value to the sum of digits.
    4. Convert the sum of digits to a binary string using the built-in bin() function.
    5. Return the binary string as the result.

    Note: Be mindful of the input constraints (0 ≤ N ≤ 10000) and the expected output format (a string of binary number)."""
    # Step 1: Convert the input number N to a string
    N_str = str(N)
    
    # Step 2: Initialize a variable to store the sum of digits
    sum_of_digits = 0
    
    # Step 3: Iterate through each character (digit) in the string representation of N
    for digit in N_str:
        # Step 3a: Convert the character to an integer
        digit_int = int(digit)
        
        # Step 3b: Add the integer value to the sum of digits
        sum_of_digits += digit_int
    
    # Step 4: Convert the sum of digits to a binary string
    binary_sum = bin(sum_of_digits)[2:]
    
    # Step 5: Return the binary string as the result
    return binary_sum