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
    1. Convert the input integer N to a string to access individual digits.
    2. Initialize a variable to store the sum of the digits.
    3. Iterate through each character (digit) in the string:
       a. Convert the character back to an integer.
       b. Add the integer to the sum.
    4. Convert the sum to a binary number (using the appropriate function or operation).
    5. Remove any unnecessary prefix from the binary number (e.g., '0b').
    6. Return the binary number as a string."""
    
    # Step 1: Convert the input integer N to a string
    N_str = str(N)
    
    # Step 2: Initialize a variable to store the sum of the digits
    digit_sum = 0
    
    # Step 3: Iterate through each character (digit) in the string
    for digit in N_str:
        # Step 3a: Convert the character back to an integer
        digit_int = int(digit)
        
        # Step 3b: Add the integer to the sum
        digit_sum += digit_int
    
    # Step 4: Convert the sum to a binary number
    binary_sum = bin(digit_sum)
    
    # Step 5: Remove any unnecessary prefix from the binary number
    binary_sum = binary_sum[2:]
    
    # Step 6: Return the binary number as a string
    return binary_sum