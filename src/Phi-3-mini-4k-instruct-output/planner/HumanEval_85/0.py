def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 

    Action Plan:
    1. Understand the problem:
        - The function takes a list of integers as input
        - The goal is to add the even elements that are at odd indices
    
    2. Initialize a variable to store the sum:
        - Set the sum to 0
    
    3. Iterate through the list with a step of 2:
        - Use a loop to go through the list, starting from the first element (index 0) and incrementing by 2
    
    4. Check for even elements at odd indices:
        - Inside the loop, check if the current element is even (using the modulus operator)
        - Also, check if the current index is odd (using the modulus operator)
    
    5. Add the even elements to the sum:
        - If both conditions are met, add the current element to the sum
    
    6. Return the final sum:
        - After the loop, return the sum of the even elements at odd indices
    
    Note: Be careful with the indexing and the step size in the loop."""
    sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0 and i % 2 != 0:
            sum += lst[i]
    return sum