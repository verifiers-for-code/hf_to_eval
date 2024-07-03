def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    

    Action Plan:
    1. Convert the input number to its absolute value to handle negative numbers.
    2. Convert the number to a string to easily iterate through each digit.
    3. Initialize two counters, one for even digits and one for odd digits, to 0.
    4. Iterate through each character (digit) in the string:
       a. Convert the character back to an integer.
       b. Check if the integer is even (i.e., the remainder of the division by 2 is 0).
       c. If the digit is even, increment the even counter; otherwise, increment the odd counter.
    5. Return a tuple containing the even counter and the odd counter, in that order."""

    # Step 1: Convert the input number to its absolute value
    num = abs(num)

    # Step 2: Convert the number to a string
    num_str = str(num)

    # Step 3: Initialize two counters
    even_count = 0
    odd_count = 0

    # Step 4: Iterate through each character (digit) in the string
    for digit in num_str:
        # Convert the character back to an integer
        digit_int = int(digit)

        # Check if the integer is even
        if digit_int % 2 == 0:
            # Increment the even counter
            even_count += 1
        else:
            # Increment the odd counter
            odd_count += 1

    # Step 5: Return a tuple containing the even counter and the odd counter
    return (even_count, odd_count)