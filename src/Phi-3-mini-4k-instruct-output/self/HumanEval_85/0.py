def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    

    Action Plan:
    1. Define a function to add even elements at odd indices:
        a. Initialize sum to 0
        b. Iterate through the list using enumerate() to get both elements and their indices
    
    2. Within the loop, check if the index is odd and the number is even:
        a. If both conditions are true, add the number to the sum
    
    3. After iterating through the list, return the sum"""
    
    # Initialize sum to 0
    sum = 0
    
    # Iterate through the list using enumerate() to get both elements and their indices
    for i, num in enumerate(lst):
        # Check if the index is odd and the number is even
        if i % 2 == 1 and num % 2 == 0:
            # Add the number to the sum
            sum += num
    
    # Return the sum
    return sum