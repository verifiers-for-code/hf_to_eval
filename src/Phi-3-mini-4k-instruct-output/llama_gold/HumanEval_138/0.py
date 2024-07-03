def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    

    Action Plan:
    1. Determine if the given number n is even by checking if it's divisible by 2.
    2. Since we need to express n as the sum of 4 positive even numbers, the minimum sum would be 4*2 = 8. 
       Check if n is greater than or equal to 8.
    3. Combine the above conditions using a logical AND operation.
    4. Return the result of the combined condition, which will be True if n can be written as the sum of exactly 4 positive even numbers, and False otherwise."""
    
    # Step 1: Check if n is even
    if n % 2 == 0:
        # Step 2: Check if n is greater than or equal to 8
        if n >= 8:
            # Step 3: Combine the above conditions using a logical AND operation
            return True
    # Step 4: Return False if the conditions are not met
    return False