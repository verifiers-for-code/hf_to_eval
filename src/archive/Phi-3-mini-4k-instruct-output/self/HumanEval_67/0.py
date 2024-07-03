def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains apples, oranges, and mango fruits.
    Given the string that represents the total number of the oranges and apples and an integer 
    that represent the total number of the fruits in the basket, return the number of the mango fruits in the basket.
    """
    # Step 1: Parse the input string to extract the quantities of apples and oranges
    parts = s.split(" and ")
    if len(parts) != 2:
        raise ValueError("Invalid input format. Expected format: 'X apples and Y oranges'")
    
    apples_str, oranges_str = parts
    apples_str = apples_str.split()
    oranges_str = oranges_str.split()
    
    # Step 2: Convert the extracted string values to integers, with error checking
    try:
        apples = int(apples_str[0])
        oranges = int(oranges_str[0])
    except ValueError:
        raise ValueError("Invalid input format. Expected numeric values for apples and oranges.")
    
    # Step 3: Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    # Step 4: Edge cases
    if mangoes < 0:
        raise ValueError("Invalid input. The sum of apples and oranges exceeds the total fruit count.")
    
    return mangoes