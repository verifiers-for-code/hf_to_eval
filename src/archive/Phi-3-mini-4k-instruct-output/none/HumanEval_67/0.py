import re
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains apples, oranges, and mango fruits.
    Given the string that represents the total number of the oranges and apples and an integer 
    that represent the total number of the fruits in the basket, return the number of the mango fruits in the basket.
    """
    # Extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    apples = int(apples_oranges[0])
    oranges = int(apples_oranges[1])
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes