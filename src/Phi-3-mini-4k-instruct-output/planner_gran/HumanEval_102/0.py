def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Step 1: Define the function choose_num with two parameters: x and y
    # Both x and y should be positive integers

    # Step 2: Initialize a variable to store the result
    # Set the initial value to -1, assuming no even number is found
    result = -1

    # Step 3: Check if there's an even number in the range [x, y]
    # Use the modulus operator (%) to check if x is even (x % 2 == 0)
    # If x is even, return x as the result (since it's the biggest even number in the range)
    if x % 2 == 0:
        result = x

    # Step 4: If x is not even, check if y is even
    # If y is even, return y as the result
    elif y % 2 == 0:
        result = y

    # Step 5: If neither x nor y is even, return -1 to indicate no even number in the range

    # Step 6: Consider handling edge cases
    # What if x and y are equal? (e.g., return x)
    # What if x is greater than y? (e.g., swap x and y)
    if x == y:
        result = x
    elif x > y:
        x, y = y, x

    # Step 7: Implement the function with the above steps
    # Use conditional statements (if-else) to check the conditions and return the result