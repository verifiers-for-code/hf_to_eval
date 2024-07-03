def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Action Plan:
    1. Handle the special case:
       - If n is 1, there's only one number (1) that satisfies the condition.
       - Return 1 for this case.

    2. For n > 1:
       a. Calculate the count of n-digit numbers starting with 1:
          - Consider the first digit is fixed (1), and the rest can be any digit (0-9).
          - Hint: Use powers of 10 to represent the possible combinations for the rest of the digits.

       b. Calculate the count of n-digit numbers ending with 1:
          - Consider the last digit is fixed (1), and the rest can be any digit (1-9 for the first digit, 0-9 for others).
          - This count is the same as numbers starting with 1.

       c. Adjust for double-counting:
          - Numbers like 101, 1001, etc., are counted twice in steps a and b.
          - Instead of subtracting, consider combining steps a and b in a way that automatically accounts for this.

    3. Combine the calculations from step 2 into a single expression:
       - Hint: The total count will be less than simply adding the results from 2a and 2b.
       - Think about how to represent this efficiently using multiplication and exponentiation.

    4. Return the final count.
    """
    if n == 1:
        return 1
    else:
        # Count of n-digit numbers starting with 1
        start_with_one = 9 * (10 ** (n - 1))

        # Count of n-digit numbers ending with 1
        end_with_one = 9 * (10 ** (n - 1))

        # Combine the counts, adjusting for double-counting
        total_count = start_with_one + end_with_one - (9 * (10 ** (n - 2)))

        return total_count