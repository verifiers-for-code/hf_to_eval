def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    

    Action Plan:
    1. Initialize an empty list to store the result.
    2. Iterate through the range from 1 to n (inclusive):
       a. For each index i:
          - If i is even:
             - Calculate the factorial of i by multiplying numbers from 1 to i.
             - Add the calculated factorial to the result list.
          - If i is odd:
             - Calculate the sum of numbers from 1 to i.
             - Add the calculated sum to the result list.
    3. Return the result list containing the calculated values for each index."""
    
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