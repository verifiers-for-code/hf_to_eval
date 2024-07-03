def strlen(string: str) -> int:
    """
    Return length of given string
    
    This function takes a string as input and returns its length.
    
    Input:
    - string (str): The input string whose length is to be calculated.
    
    Output:
    - int: The length of the input string.
    
    The function works by using the built-in `len()` function to calculate the length of the input string.
    
    Action Plan:
    1. Document the function:
        - Describe the function's purpose
        - Include the input and output types
        - Provide a summary of how the function works
    
    2. Input validation:
        - Check if the input is a string
        - Return a specific value (e.g., -1 or None) for non-string inputs
    
    3. Calculate the string's length:
        - Use the built-in `len()` function
    
    4. Return the length:
        - Return the length of the string if it's valid
    
    5. Edge cases to handle:
        - Empty string
        - Non-string inputs
        - Consider the behavior of the `len()` function for strings of different lengths
    """
    if not isinstance(string, str):
        return -1
    return len(string)