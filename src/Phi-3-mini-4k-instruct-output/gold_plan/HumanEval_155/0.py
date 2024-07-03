def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)

    Action Plan:
    1. Initialize two variables to count even and odd digits, both set to 0.
    2. Convert the absolute value of the input number to a string to iterate through its digits.
    3. Iterate through each character (digit) in the string:
        a. Convert the character back to an integer.
        b. Check if the integer is even or odd using the modulo operator (% 2).
        c. Increment the appropriate counter based on whether the digit is even or odd.
    4. After the iteration, return a tuple containing the even count and odd count.

    Note: Remember to handle both positive and negative input numbers.
    """
    even_count = 0
    odd_count = 0
    num = abs(num)
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)