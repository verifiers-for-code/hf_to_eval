def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    

    Action Plan:
    1. Initialize a variable to store the sum of odd elements at even positions.
    2. Iterate through the input list with indexing:
       a. Check if the current index is even (i.e., the position is even).
       b. If the position is even, check if the element at that position is odd.
       c. If both conditions are true, add the element to the sum variable.
    3. Return the final sum of odd elements at even positions."""
    
    # Initialize a variable to store the sum of odd elements at even positions
    sum_odd_even_pos = 0
    
    # Iterate through the input list with indexing
    for i in range(len(lst)):
        # Check if the current index is even (i.e., the position is even)
        if i % 2 == 0:
            # If the position is even, check if the element at that position is odd
            if lst[i] % 2 != 0:
                # If both conditions are true, add the element to the sum variable
                sum_odd_even_pos += lst[i]
    
    # Return the final sum of odd elements at even positions
    return sum_odd_even_pos