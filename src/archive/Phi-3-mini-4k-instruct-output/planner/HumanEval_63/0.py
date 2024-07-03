def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is less than 0.

    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    # Step 1: Define the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Step 2: Set up a dynamic programming approach
    fibfib_values = [0, 0, 1]  # Initialize the list with the base cases

    # Step 3: Implement the recursive formula
    for i in range(3, n + 1):
        fibfib_values.append(fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3])

    # Step 4: Handle edge cases
    if n < 0:
        raise ValueError("n must be non-negative")

    # Step 5: Return the result
    return fibfib_values[n]