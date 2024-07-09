def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    

    Action Plan:
    1. Convert the input number to a string to easily access each digit.
    2. Initialize two counters, one for even digits and one for odd digits, to 0.
    3. Iterate through each character (digit) in the string:
        a. Convert the character back to an integer.
        b. Check if the digit is even by using the modulus operator (%).
        c. If the digit is even, increment the even counter.
        d. If the digit is odd, increment the odd counter.
    4. After iterating through all digits, return a tuple containing the even and odd counters.
    5. Ensure the function handles negative numbers correctly by considering the absolute value of the input.
    
    Note: Be mindful of the data types and conversions between integers and strings."""

    # Convert the input number to a string
    num_str = str(abs(num))

    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0

    # Iterate through each character (digit) in the string
    for digit in num_str:
        # Convert the character back to an integer
        digit_int = int(digit)

        # Check if the digit is even
        if digit_int % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Return a tuple containing the even and odd counters
    return (even_count, odd_count)