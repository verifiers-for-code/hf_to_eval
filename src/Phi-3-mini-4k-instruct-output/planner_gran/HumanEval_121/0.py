def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    

    1. Initialize a variable to store the sum of the odd elements in even positions
       - Set the initial value to 0
    
    2. Iterate through the input list, considering each element and its index:
       a. Check if the current index is even (i.e., the index is divisible by 2)
       b. Check if the current element is odd (i.e., the element is not divisible by 2)
       c. If both conditions are met, add the element to the sum variable
    
    3. Continue iterating through the list until all elements have been processed
    
    4. Return the final sum of the odd elements in even positions
    
    Implementation details:
    - Use a for loop to iterate through the list with both the element and its index
    - Use the modulus operator (%) to check for even indices and odd elements
    - Use the += operator to add elements to the sum variable
    - Ensure the function handles empty input lists correctly
    - Consider adding input validation to ensure the input is a non-empty list of integers"""
    if not lst or not all(isinstance(x, int) for x in lst):
        return 0
    sum_odd_even = 0
    for i, x in enumerate(lst):
        if i % 2 == 0 and x % 2 != 0:
            sum_odd_even += x
    return sum_odd_even