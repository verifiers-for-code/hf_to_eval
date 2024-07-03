def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
    Action Plan:
    1. Initialize a variable to store the largest divisor:
       - Set the initial value to 0 or a default value
    
    2. Iterate from n-1 to 1 (inclusive):
       - Use a for loop with a range from n-1 to 0, decrementing by 1
    
    3. For each number i in the iteration:
       a. Check if n is divisible by i:
          - Use the modulus operator (%) to check for divisibility
          - If n % i == 0, then i is a divisor of n
       b. If i is a divisor and larger than the current largest divisor:
          - Update the largest divisor to be i
    
    4. After the iteration, return the largest divisor:
       - The largest divisor is the largest number that divides n evenly, smaller than n
    
    Additional implementation details:
    - Use a for loop to iterate from n-1 to 1
    - Use the modulus operator (%) to check for divisibility
    - Update the largest divisor variable when a larger divisor is found
    - Return the largest divisor at the end of the function
    - Ensure the function handles edge cases, such as n being 0 or 1"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        largest_divisor = 0
        for i in range(n-1, 0, -1):
            if n % i == 0:
                largest_divisor = i
                break
        return largest_divisor