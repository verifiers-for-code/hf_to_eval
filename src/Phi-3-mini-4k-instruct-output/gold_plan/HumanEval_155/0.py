def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Step 1: Initialize two variables to count even and odd digits, both set to 0.
    even_count = 0
    odd_count = 0

    # Step 2: Convert the absolute value of the input number to a string to iterate through its digits.
    num_str = str(abs(num))

    # Step 3: Iterate through each character (digit) in the string
    for digit in num_str:
        # Convert the character back to an integer
        digit_int = int(digit)

        # Step 3a: Check if the integer is even or odd using the modulo operator (% 2)
        if digit_int % 2 == 0:
            # Step 3b: Increment the appropriate counter based on whether the digit is even or odd
            even_count += 1
        else:
            odd_count += 1

    # Step 4: Return a tuple containing the even count and odd count
    return (even_count, odd_count)