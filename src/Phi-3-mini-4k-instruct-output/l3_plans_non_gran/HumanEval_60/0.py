def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    

    Action Plan:
    1. Define a function named `sum_to_n` that takes a single integer parameter `n`.
    2. Initialize a variable `total` to 0, which will store the sum of numbers from 1 to `n`.
    3. Create a loop that iterates from 1 to `n` (inclusive) using a range function.
    4. Within the loop, add each number to the `total` variable.
    5. After the loop, return the final value of `total`, which is the sum of numbers from 1 to `n`.
    6. Consider handling edge cases, such as `n` being 0 or negative.
    
    Note: Use a simple and efficient approach to calculate the sum, such as a loop or a built-in function."""
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n+1):
        total += i
    return total