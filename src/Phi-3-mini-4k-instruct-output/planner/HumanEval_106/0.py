def f(n):
    """Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    The factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]

    Action Plan:
    1. Understand the problem requirements:
        - The function takes an integer n as input
        - The function returns a list of size n
        - The value at index i is the factorial of i if i is even
        - The value at index i is the sum of numbers from 1 to i if i is odd
    
    2. Initialize an empty list to store the result
    
    3. Implement a loop to iterate from 1 to n (inclusive)
        - For each iteration, check if the current index i is even or odd
    
    4. Calculate the factorial for even indices:
        - If i is even, calculate the factorial of i (i * (i-1) *... * 1)
        - Append the calculated factorial to the result list
    
    5. Calculate the sum for odd indices:
        - If i is odd, calculate the sum of numbers from 1 to i (1 + 2 +... + i)
        - Append the calculated sum to the result list
    
    6. Return the final result list
    
    Note: Use appropriate mathematical operations and conditional statements to implement the logic.
    Be careful with the indexing and calculations for even and odd indices."""
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            sum_of_numbers = sum(range(1, i+1))
            result.append(sum_of_numbers)
    return result