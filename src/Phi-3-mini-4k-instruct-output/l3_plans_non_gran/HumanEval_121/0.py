def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    

    Action Plan:
    1. Initialize a variable to store the sum of odd elements in even positions (initially 0).
    2. Determine the length of the input list (n).
    3. Iterate through the list using a loop that runs n//2 times (since we're considering even positions).
    4. Inside the loop, check each element at index 2*i (where i is the current iteration):
        a. Check if the element is odd (using the modulus operator %).
        b. If the element is odd, add it to the sum.
    5. After the loop, return the final sum of odd elements in even positions.
    
    Note: Consider the indexing and the even position constraint (2*i).
    Be careful with the loop range and the indexing."""
    
    # Step 1: Initialize a variable to store the sum of odd elements in even positions
    sum_odd_even_pos = 0
    
    # Step 2: Determine the length of the input list (n)
    n = len(lst)
    
    # Step 3: Iterate through the list using a loop that runs n//2 times
    for i in range(n//2):
        # Step 4: Check each element at index 2*i
        if lst[2*i] % 2 != 0:
            # Step 4a: Check if the element is odd
            # Step 4b: If the element is odd, add it to the sum
            sum_odd_even_pos += lst[2*i]
    
    # Step 5: Return the final sum of odd elements in even positions
    return sum_odd_even_pos