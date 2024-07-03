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
    1. Parse the input string to extract the number of apples and oranges:
        - Identify the pattern in the string (e.g., "X apples and Y oranges")
        - Use string methods to extract the numbers (e.g., `split`, `strip`, `int`)
    
    2. Calculate the total number of apples and oranges:
        - Add the extracted numbers of apples and oranges
    
    3. Calculate the number of mango fruits:
        - Subtract the total number of apples and oranges from the total number of fruits in the basket
    
    4. Return the result:
        - Return the calculated number of mango fruits
    
    Note: Be careful when extracting numbers from the input string to avoid errors.
    Use appropriate string methods and data types to ensure correct calculations.
    """
    # Step 1: Parse the input string to extract the number of apples and oranges
    words = s.split()
    apples = int(words[1].strip(" apples"))
    oranges = int(words[3].strip(" oranges"))
    
    # Step 2: Calculate the total number of apples and oranges
    total_apples_oranges = apples + oranges
    
    # Step 3: Calculate the number of mango fruits
    mango_fruits = n - total_apples_oranges
    
    # Step 4: Return the result
    return mango_fruits