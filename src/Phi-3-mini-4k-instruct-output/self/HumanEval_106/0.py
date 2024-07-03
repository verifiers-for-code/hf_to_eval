def f(n):
    """Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    The factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
    Action Plan:
    1. Define the function f with the parameter n
    
    2. Initialize an empty list of size n
    
    3. Iterate over the range from 1 to n (inclusive) to generate the list
    
    4. Check if the current index is even:
        a. If yes, calculate the factorial of the index
        b. Store the result in the list at the current index
    
    5. If the current index is odd:
        a. Calculate the sum of numbers from 1 to the current index
        b. Store the result in the list at the current index
    
    6. Use the factorial function (either defined or imported from a math module) and the range function for calculations.
    
    7. Test the function with the given example example: f(5) should return [1, 2, 6, 24, 15]"""
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result