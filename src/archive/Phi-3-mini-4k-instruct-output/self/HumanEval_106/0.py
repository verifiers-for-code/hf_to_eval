def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Step 2: Initialize an empty list of size n
    result = [0] * n

    # Step 3: Iterate over the range from 1 to n (inclusive) to generate the list
    for i in range(1, n + 1):
        # Step 4: Check if the current index is even
        if i % 2 == 0:
            # Calculate the factorial of the index
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            # Store the result in the list at the current index
            result[i - 1] = factorial
        else:
            # Calculate the sum of numbers from 1 to the current index
            result[i - 1] = sum(range(1, i + 1))

    return result