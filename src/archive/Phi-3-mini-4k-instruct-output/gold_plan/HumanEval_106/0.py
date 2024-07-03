def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]

    Action Plan:
    1. Initialize an empty list to store the results.
    2. Iterate through the range of numbers from 1 to n (inclusive).
    3. For each number i in the range:
       a. Check if i is even or odd.
       b. If i is even:
          - Calculate the factorial of i (multiply all numbers from 1 to i).
          - Append the result to the list.
       c. If i is odd:
          - Calculate the sum of all numbers from 1 to i.
          - Append the result to the list.
    4. Return the final list.

    Note: Remember that the index i starts from 1, so adjust your loop accordingly.
    """
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