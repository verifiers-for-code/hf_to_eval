def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    

    Action Plan:
    1. Input validation:
        a. Check if x and y are positive integers
    
    2. Range check:
        a. If x > y, return -1, as no even number will be within the range [x, y]
    
    3. Iteration through the range:
        a. Generate a list of even numbers within the range using a loop or list comprehension
        b. Filter out numbers outside the range if needed
    
    4. Handling the absence of an even number:
        a. If the generated list is empty, return -1
    
    5. Finding the maximum even number:
        a. Use the max() function on the list of even numbers
    
    6. Considerations for efficiency:
        a. Only generate even numbers within the range to minimize processing
    
    7. Testing:
        a. Ensure correct behavior with various test cases"""

    # Input validation
    if not (isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0):
        return -1

    # Range check
    if x > y:
        return -1

    # Generate a list of even numbers within the range
    even_numbers = [num for num in range(x, y + 1) if num % 2 == 0]

    # Handling the absence of an even number
    if not even_numbers:
        return -1

    # Finding the maximum even number
    return max(even_numbers)