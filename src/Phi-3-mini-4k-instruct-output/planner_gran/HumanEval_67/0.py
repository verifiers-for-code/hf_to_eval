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
    
    1. Initialize variables to store the number of apples and oranges:
       - Initialize two variables, `apples` and `oranges`, to store the extracted values
    
    2. Process the input string:
       - Split the input string into a list of words using a space as the separator
       - Iterate through the list of words:
         a. Check if the current word is an integer (using the `isdigit()` method)
         b. If it is, check if the word ends with "apples" or "oranges" (case-insensitive)
         c. If it does, extract the integer value from the word and store it in the corresponding variable (`apples` or `oranges`)
    
    3. Calculate the number of mango fruits:
       - Subtract the number of apples and oranges from the total number of fruits in the basket (`n`)
    
    4. Return the result:
       - Return the calculated number of mango fruits as an integer
    
    Additional implementation details:
    - Use a loop or list comprehension to iterate through the words in the input string
    - Use conditional statements to check if a word is an integer and if it ends with "apples" or "oranges"
    - Use the `isdigit()` method to check if a word is an integer
    - Use the `lower()` method to make the check case-insensitive
    - Handle edge cases, such as an empty input string or invalid input values"""
    
    # Initialize variables to store the number of apples and oranges
    apples = 0
    oranges = 0
    
    # Process the input string
    words = s.split()
    for word in words:
        if word.isdigit():
            if word.lower().endswith("apples"):
                apples = int(word)
            elif word.lower().endswith("oranges"):
                oranges = int(word)
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    # Return the result
    return mangoes