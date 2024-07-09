def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    

    Action Plan:
    1. Define the function choose_num with two parameters, x and y, which are both positive integers.
    2. Initialize a variable to store the largest even number found in the range [x, y].
    3. Iterate through the range from x to y (inclusive) using a loop:
        a. Check if the current number is even (using the modulus operator %).
        b. If the number is even, update the largest even number variable if the current number is greater.
    4. After the loop, check if the largest even number variable is still -1 (default value).
        a. If it is, return -1 to indicate that no even number was found in the range.
        b. Otherwise, return the largest even number found in the range.
    5. Ensure the function handles edge cases, such as when x and y are the same or when y is less than x.
    
    Note: Use appropriate conditional statements and loops to implement the logic.
    Be careful when handling the edge cases and returning the correct result."""
    
    # Initialize the largest even number to -1
    largest_even = -1
    
    # Iterate through the range from x to y (inclusive)
    for num in range(x, y + 1):
        # Check if the current number is even
        if num % 2 == 0:
            # Update the largest even number if the current number is greater
            if num > largest_even:
                largest_even = num
    
    # Check if the largest even number is still -1
    if largest_even == -1:
        return -1
    else:
        return largest_even