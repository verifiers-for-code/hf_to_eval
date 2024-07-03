def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains apples, oranges, and mango fruits.
    Given the string that represents the total number of oranges and apples and an integer that represent
    the total number of the fruits in the basket, return the number of mango fruits in the basket.

    Parameters:
    s (str): A string representing the number of apples and oranges in the format "X apples and Y oranges"
    n (int): The total number of fruits in the basket

    Returns:
    int: The number of mango fruits in the basket

    Example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 95
    fruit_distribution("100 apples and 1 orange", 120) -> 19
    """
    # Step 1: Parse the input string to extract the number of apples and oranges
    parts = s.split(" and ")
    apples_str, oranges_str = parts[0].split(" ")
    apples_str = apples_str.replace("apples", "").strip()
    oranges_str = oranges_str.replace("oranges", "").strip()

    apples = int(apples_str)
    oranges = int(oranges_str)

    # Step 2: Calculate the total number of apples and oranges
    total_apples_oranges = apples + oranges

    # Step 3: Calculate the number of mango fruits
    mango_fruits = n - total_apples_oranges

    # Step 4: Return the result
    return mango_fruits