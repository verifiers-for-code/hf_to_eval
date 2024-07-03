def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Action Plan:
    # 1. Understand that we need to find the largest number that divides the input number 'n' evenly, which is smaller than 'n'.
    # 2. Define the search space for the largest divisor as all numbers from 'n-1' down to 1.
    # 3. Iterate through the search space in reverse order (from largest to smallest).
    # 4. For each number in the search space, check if it divides 'n' evenly (i.e., the remainder of 'n' divided by the number is 0).
    # 5. As soon as a number is found that divides 'n' evenly, return that number as the largest divisor.
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1