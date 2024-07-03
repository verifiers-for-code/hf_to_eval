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
    1. Convert the input integer N to a string to iterate through its digits.
    2. Create a list of integers by converting each character in the string back to an integer.
    3. Use the sum() function to calculate the total sum of all digits.
    4. Convert the sum to its binary representation using the bin() function.
    5. Remove the '0b' prefix from the binary string to get the final result.
    6. Return the resulting binary string.

    Hint: Consider using a list comprehension for steps 1-2 and string slicing for step 5.
    """
    # Step 1: Convert the input integer N to a string
    N_str = str(N)
    
    # Step 2: Create a list of integers by converting each character in the string back to an integer
    digits = [int(digit) for digit in N_str]
    
    # Step 3: Calculate the total sum of all digits
    total_sum = sum(digits)
    
    # Step 4: Convert the sum to its binary representation
    binary_sum = bin(total_sum)
    
    # Step 5: Remove the '0b' prefix from the binary string
    result = binary_sum[2:]
    
    # Step 6: Return the resulting binary string
    return result