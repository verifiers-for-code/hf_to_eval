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
    1. Implement a helper function to check if a number has even digits:
        a. Use the modulo operator (%) to check for evenness
        b. Iterate through each digit of the number
    
    2. In the main function:
        a. Use list comprehension to apply the helper function to each number in the input list
        b. Filter numbers without any even digits
        c. Sort the filtered list
    
    3. Edge cases to consider:
        a. Input with numbers containing even digits
        b. Input with numbers containing only odd digits
        c. Input with zero
    
    4. Testing:
        - Verify the function works as expected with the provided test cases"""

    def has_even_digit(n):
        """Helper function to check if a number has even digits."""
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False

    # Filter numbers without any even digits and sort the result
    return sorted([num for num in x if not has_even_digit(num)])