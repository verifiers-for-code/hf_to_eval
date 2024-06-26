def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Step 1: Initialize a container to store numbers meeting the criteria
    numbers = []

    # Step 2: Iterate through numbers from 0 to n-1
    for i in range(n):
        # Check if the current number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            numbers.append(i)

    # Step 3: Convert the collected numbers to a single string
    numbers_str = ''.join(map(str, numbers))

    # Step 4: Count the occurrences of '7' in the resulting string
    count_7 = numbers_str.count('7')

    # Return the final count
    return count_7