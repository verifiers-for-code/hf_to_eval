def f(n):
    """Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    The factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
    1. Define the function f with a single parameter n
       - The function takes an integer n as input
    
    2. Create an empty list to store the result
       - Initialize an empty list to hold the calculated elements
    
    3. Iterate over the range from 1 to n (inclusive)
       - Use a for loop to iterate over the range from 1 to n
    
    4. Apply the conditions to each element in the list:
       a. If the index i is even:
          - Calculate the factorial of i (i * (i-1) *... * 1)
          - Append the factorial to the result list
       b. If the index i is odd:
          - Calculate the sum of numbers from 1 to i (1 + 2 +... + i)
          - Append the sum to the result list
    
    5. Return the final list
       - After iterating over the entire range, return the completed list
    
    Additional implementation details:
    - Use a for loop or list comprehension to iterate over the range
    - Use conditional statements (if-else) to apply the conditions
    - Use mathematical operations to calculate the factorial and sum of numbers
    - Ensure the function handles edge cases, such as n being 0 or 1"""
    
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