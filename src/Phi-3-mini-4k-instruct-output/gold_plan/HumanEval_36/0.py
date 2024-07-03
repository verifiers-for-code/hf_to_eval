def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3

    Action Plan:
    1. Initialize a container to store numbers meeting the criteria.
    2. Iterate through numbers from 0 to n-1:
       a. Check if the current number is divisible by 11 or 13.
       b. If yes, add it to the container.
    3. Convert the collected numbers to a single string:
       a. Convert each number in the container to a string.
       b. Join all these strings together.
    4. Count the occurrences of '7' in the resulting string:
       a. Initialize a counter for '7's.
       b. Iterate through each character in the string.
       c. Increment the counter when '7' is encountered.
    5. Return the final count.
    """
    container = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            container.append(str(i))
    string = ''.join(container)
    count = 0
    for char in string:
        if char == '7':
            count += 1
    return count