def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    

    Action Plan:
    1. Split the input string into words using spaces as separators.
    2. Initialize an empty list to store the numbers of apples and oranges.
    3. Iterate through each word in the split string:
       a. Check if the word is a digit (using a suitable method).
       b. If it's a digit, convert it to an integer and add it to the list.
    4. Calculate the number of mangoes by subtracting the sum of the numbers in the list from the total number of fruits (n).
    5. Return the result, which represents the number of mangoes in the basket."""

    # Step 1: Split the input string into words using spaces as separators
    words = s.split()

    # Step 2: Initialize an empty list to store the numbers of apples and oranges
    fruit_numbers = []

    # Step 3: Iterate through each word in the split string
    for word in words:
        # Check if the word is a digit (using a suitable method)
        if word.isdigit():
            # If it's a digit, convert it to an integer and add it to the list
            fruit_numbers.append(int(word))

    # Step 4: Calculate the number of mangoes by subtracting the sum of the numbers in the list from the total number of fruits (n)
    mangoes = n - sum(fruit_numbers)

    # Step 5: Return the result, which represents the number of mangoes in the basket
    return mangoes