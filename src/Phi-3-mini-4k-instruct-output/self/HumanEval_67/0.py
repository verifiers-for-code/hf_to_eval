def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    

    Action Plan:
    1. Parse the input string to extract the quantities of apples and oranges:
        - Use string manipulation methods to split the string and find relevant parts.
    
    2. Convert the extracted string values to integers, with error checking:
        - Make sure to handle cases with non-numeric parts (e.g., "100 apples and 1 orange").
    
    3. Calculate the number of mangoes:
        - Subtract the sum of apples and oranges from the total fruit count.
    
    4. Edge cases:
        - Validate input string format (e.g., "100 apples and 1 orange").
        - Handle scenarios with zero apples, oranges, or total fruits.
    
    5. Function structure:
        - Separate parsing and conversion logic from calculation logic.
        - Ensure single responsibility for each function (e.g., one function for parsing, one for conversion).
    
    6. Return the calculated number of mangoes."""
    
    # Step 1: Parse the input string to extract the quantities of apples and oranges
    parts = s.split(" and ")
    if len(parts) != 2:
        raise ValueError("Invalid input string format")
    
    apple_str, orange_str = parts
    apple_str = apple_str.split()[0]
    orange_str = orange_str.split()[0]
    
    # Step 2: Convert the extracted string values to integers, with error checking
    try:
        apple_count = int(apple_str)
        orange_count = int(orange_str)
    except ValueError:
        raise ValueError("Invalid input string format")
    
    # Step 3: Calculate the number of mangoes
    mango_count = n - apple_count - orange_count
    
    # Step 4: Edge cases
    if mango_count < 0:
        raise ValueError("Total fruit count is less than the sum of apples and oranges")
    
    # Step 5: Function structure
    # Separate parsing and conversion logic from calculation logic
    # Ensure single responsibility for each function
    
    # Step 6: Return the calculated number of mangoes
    return mango_count