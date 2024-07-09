import re

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
    1. Split the input string into two parts using the 'and' keyword as the separator.
    2. Extract the numbers of apples and oranges from the two parts of the string using regular expressions or string methods.
    3. Convert the extracted numbers to integers.
    4. Calculate the total number of fruits in the basket by adding the numbers of apples and oranges.
    5. Subtract the total number of fruits from the total number of fruits in the basket.
    6. Return the result as the number of mango fruits in the basket.
    
    Note: Use appropriate string methods and regular expressions for parsing the input string.
    Be careful when converting the extracted numbers to integers.
    """
    # Step 1: Split the input string into two parts using the 'and' keyword as the separator
    parts = s.split(" and ")
    
    # Step 2: Extract the numbers of apples and oranges from the two parts of the string using regular expressions
    apples = int(re.findall(r'\d+', parts[0])[0])
    oranges = int(re.findall(r'\d+', parts[1])[0])
    
    # Step 3: Convert the extracted numbers to integers
    # (already done in Step 2)
    
    # Step 4: Calculate the total number of fruits in the basket by adding the numbers of apples and oranges
    total_fruits = apples + oranges
    
    # Step 5: Subtract the total number of fruits from the total number of fruits in the basket
    mango_fruits = n - total_fruits
    
    # Step 6: Return the result as the number of mango fruits in the basket
    return mango_fruits