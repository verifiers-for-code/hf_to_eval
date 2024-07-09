def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    

    Action Plan:
    1. Initialize an empty list to store the unique numbers with no even digits.
    2. Iterate through each number in the input list:
        a. Convert the number to a string to access its digits.
        b. Check if all digits in the number are odd:
            - Use a conditional statement to check if any digit is even (e.g., `any(int(digit) % 2 == 0 for digit in num_str)`).
            - If no even digits are found, add the original number to the unique numbers list.
    3. Sort the unique numbers list in ascending order.
    4. Return the sorted list of unique numbers with no even digits.
    
    Note: Be careful when converting between string and integer types.
    Use appropriate conditional statements and list operations to achieve the desired result."""
    unique_numbers = []
    for num in x:
        num_str = str(num)
        if not any(int(digit) % 2 == 0 for digit in num_str):
            unique_numbers.append(num)
    unique_numbers.sort()
    return unique_numbers