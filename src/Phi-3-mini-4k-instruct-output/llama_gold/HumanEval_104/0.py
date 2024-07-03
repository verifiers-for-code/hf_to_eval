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
    1. Initialize an empty list to store elements with only odd digits.
    2. Iterate through each element in the input list:
       a. Convert the element to a string to access individual digits.
       b. Check each digit in the string:
          - Convert the digit back to an integer.
          - Verify if the digit is odd (i.e., the remainder of the digit divided by 2 is 1).
          - If all digits are odd, add the original element to the result list.
    3. Sort the result list in increasing order.
    4. Return the sorted list of elements with only odd digits."""

    result = []
    for num in x:
        digits = str(num)
        if all(int(digit) % 2 == 1 for digit in digits):
            result.append(num)
    result.sort()
    return result