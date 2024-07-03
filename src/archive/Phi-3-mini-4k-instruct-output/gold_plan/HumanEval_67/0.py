def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains apples, oranges, and mango fruits.
    Given the string that represents the total number of the oranges and apples and an integer 
    that represent the total number of the fruits in the basket, return the number of the mango fruits in the basket.
    For example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    """
    # Step 1: Initialize an empty list to store the numbers of apples and oranges.
    fruit_counts = []

    # Step 2: Split the input string 's' into individual words.
    words = s.split()

    # Step 3: Iterate through each word in the split string.
    for word in words:
        # Step 3a: Check if the word is a digit (represents a number).
        if word.isdigit():
            # Step 3b: Convert it to an integer and add it to the list.
            fruit_counts.append(int(word))

    # Step 4: Calculate the sum of all numbers in the list (total apples and oranges).
    total_apples_oranges = sum(fruit_counts)

    # Step 5: Subtract this sum from the total number of fruits 'n' to get the number of mangoes.
    mangoes = n - total_apples_oranges

    # Step 6: Return the result (number of mangoes).
    return mangoes