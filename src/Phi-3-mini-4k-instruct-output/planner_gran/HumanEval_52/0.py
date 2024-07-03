def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    

    1. Understand the input parameters:
       - The function takes two parameters: a list of numbers (l) and a threshold value (t)
       - The list can contain any number of elements, and the threshold is a single integer value
    
    2. Initialize a variable to store the result:
       - Set a boolean variable (e.g., all_below) to True, assuming all numbers are below the threshold initially
    
    3. Iterate through each number in the list:
       - Use a loop to process each number in the list
       - For each number, check if it is below the threshold
       - If the number is not below the threshold:
          - Set the result variable to False
          - Break out of the loop, as we've found a number that's not below the threshold
    
    4. Return the result:
       - If the loop completes without finding any number above the threshold:
          - Return True, indicating all numbers are below the threshold
       - If the loop found a number above the threshold:
          - Return False, indicating not all numbers are below the threshold
    
    Additional implementation details:
    - Use a for loop to iterate through the list of numbers
    - Use an if statement to check if a number is below the threshold
    - Use a boolean variable to store the result and update it accordingly
    - Return the result at the end of the function"""
    all_below = True
    for num in l:
        if num >= t:
            all_below = False
            break
    return all_below