def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    

    Action Plan:
    1. Check the input number 'n' to ensure it is a positive integer:
        - Return False if 'n' is not positive
    
    2. Iterate over a range of possible even numbers starting from 2 until the sum of four even numbers would exceed 'n'
        - For each even number 'even_num' in the range, do the following:
            a. Check that 'even_num' is at most 'n/4' (as we are looking for only 4 even numbers)
            b. Create a loop to find three more distinct even numbers that add up to 'n - even_num'
            c. If three even numbers exist, return True
    
    3. If no valid combination is found after the loop, return False"""
    
    # Check if n is a positive integer
    if n <= 0:
        return False
    
    # Iterate over a range of possible even numbers
    for even_num in range(2, n//4 + 1, 2):
        # Check if even_num is at most n/4
        if even_num > n//4:
            break
        
        # Find three more distinct even numbers that add up to n - even_num
        for i in range(even_num + 2, n - even_num, 2):
            for j in range(i + 2, n - even_num - i, 2):
                k = n - even_num - i - j
                if k > j and k > i and k > even_num:
                    return True
    
    # If no valid combination is found, return False
    return False