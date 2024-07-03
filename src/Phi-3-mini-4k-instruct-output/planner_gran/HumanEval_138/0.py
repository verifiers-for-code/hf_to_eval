def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    

    1. Understand the problem:
       - The function takes an integer `n` as input
       - It needs to determine if `n` can be written as the sum of exactly 4 positive even numbers
    
    2. Define the possible range of even numbers:
       - The smallest even number is 2
       - The largest even number is 8 (since the problem specifies positive even numbers, and 8 is the largest even number that can be expressed as the sum of 4 positive even numbers)
    
    3. Initialize a loop to iterate over possible combinations of 4 even numbers:
       - Use a loop variable `i` to iterate over the range of possible even numbers (2 to 8)
       - For each `i`, use another loop variable `j` to iterate over the range of possible even numbers (2 to `i-2`)
       - This ensures that we consider all possible combinations of 4 even numbers
    
    4. Check if the sum of the 4 even numbers equals the given number:
       - Inside the inner loop, check if the sum of `i` and `j` equals `n`
       - If the sum equals `n`, return `True` immediately
    
    5. Return the result:
       - If the loop completes without finding a combination that sums up to `n`, return `False`
    
    Additional implementation details:
    - Use a nested loop structure to iterate over all possible combinations of 4 even numbers
    - Use the modulo operator (`%`) to check if a number is even
    - Use the `range` function to generate the sequence of even numbers
    - Ensure that the function handles edge cases, such as `n` being 0 or a negative number"""
    
    if n <= 0:
        return False
    
    for i in range(2, 9):
        for j in range(2, i):
            if i + j + (i-2) + (i-4) == n:
                return True
    
    return False