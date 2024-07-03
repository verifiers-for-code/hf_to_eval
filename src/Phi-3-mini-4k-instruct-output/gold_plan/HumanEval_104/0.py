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
    1. Initialize an empty list to store numbers with only odd digits.
    2. Iterate through each number in the input list 'x'.
    3. For each number:
       a. Convert the number to a string to check individual digits.
       b. Check if all digits in the number are odd:
          - Use a method to verify that each character (digit) in the string,
            when converted to an integer, is odd (hint: use modulo operator).
       c. If all digits are odd, add the original number to the result list.
    4. Sort the result list in ascending order.
    5. Return the sorted list of numbers with only odd digits.

    Note: Implement the function to handle edge cases, such as empty input lists.
    """
    result = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
    return sorted(result)