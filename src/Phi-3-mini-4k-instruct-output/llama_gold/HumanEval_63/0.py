def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    

    Action Plan:
    1. Handle the base cases: return 0 for n == 0 and n == 1, and return 1 for n == 2.
    2. Initialize a data structure (e.g., a list or dictionary) to store the FibFib numbers for memoization.
    3. Initialize the first three elements of the data structure with the base case values.
    4. Iterate from 3 to n (inclusive):
       a. Calculate the current FibFib number as the sum of the three previous numbers in the data structure.
       b. Store the calculated value in the data structure.
    5. Return the nth FibFib number from the data structure."""

    # Step 1: Handle the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Step 2: Initialize a data structure for memoization
    fibfib_nums = [0, 0, 1]

    # Step 3: Initialize the first three elements of the data structure
    # This step is already done in the previous step

    # Step 4: Iterate from 3 to n (inclusive)
    for i in range(3, n + 1):
        # Calculate the current FibFib number
        current_fibfib = fibfib_nums[i - 1] + fibfib_nums[i - 2] + fibfib_nums[i - 3]

        # Store the calculated value in the data structure
        fibfib_nums.append(current_fibfib)

    # Step 5: Return the nth FibFib number from the data structure
    return fibfib_nums[n]