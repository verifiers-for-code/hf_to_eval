def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3

    Action Plan:
    1. Initialize a variable 'count' to 0 to keep track of the string length
    2. Iterate through each character in the input 'string':
       a. For each character, increment 'count' by 1
    3. After the iteration is complete, return the final value of 'count'

    Note: This plan avoids using any built-in length functions and 
    implements the length calculation manually.
    """
    count = 0
    for char in string:
        count += 1
    return count