def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Step 1: Initialize an empty list to store numbers less than n that are divisible by 11 or 13.
    divisible_numbers = []

    # Step 2: Iterate through the range of numbers from 0 to n-1:
    for i in range(n):
        # a. Check if the current number is divisible by 11 or 13.
        if i % 11 == 0 or i % 13 == 0:
            # b. If it is, add the number to the list.
            divisible_numbers.append(i)

    # Step 3: Convert the list of numbers to a string representation (e.g., by concatenating their string forms).
    numbers_str = ''.join(str(num) for num in divisible_numbers)

    # Step 4: Initialize a counter to count the occurrences of the digit 7.
    count_7 = 0

    # Step 5: Iterate through each character in the string:
    for char in numbers_str:
        # a. Check if the character is equal to '7'.
        if char == '7':
            # b. If it is, increment the counter.
            count_7 += 1

    # Step 6: Return the final count of the digit 7.
    return count_7