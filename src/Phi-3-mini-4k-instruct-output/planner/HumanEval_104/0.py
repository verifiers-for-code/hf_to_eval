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
    1. Define a helper function `has_even_digit` to check if a number has any even digit:
        a. Convert the number to a string to iterate over its digits
        b. Iterate over each digit and check if it's even (using the modulus operator)
        c. Return `True` if any even digit is found, `False` otherwise
    
    2. Define the main function `unique_digits` to process the input list:
        a. Initialize an empty list `result` to store the numbers without even digits
        b. Iterate over each number in the input list:
            i. Check if the number has no even digits using the `has_even_digit` function
            ii. If the number has no even digits, add it to the `result` list
        c. Sort the `result` list in increasing order
        d. Return the sorted `result` list
    
    3. Consider edge cases:
        a. Handle an empty input list
        b. Handle a list with no numbers without even digits
    
    4. Return the final result, which is a sorted list of numbers without even digits"""

    def has_even_digit(n):
        """Check if a number has any even digit."""
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False

    result = []
    for num in x:
        if not has_even_digit(num):
            result.append(num)

    return sorted(result)