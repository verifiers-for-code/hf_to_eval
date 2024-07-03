def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    

    Action Plan:
    1. Handle negative numbers:
        - Convert the input number to its absolute value using the `abs()` function
    
    2. Convert the number to a string:
        - Use the `str()` function to convert the number to a string
    
    3. Initialize counters for even and odd digits:
        - Initialize two variables, `even_count` and `odd_count`, to 0
    
    4. Iterate through each digit in the string:
        - Use a `for` loop to iterate through each character in the string
        - Convert each character back to an integer using the `int()` function
        - Check if the digit is even or odd using the modulus operator (`%`)
        - Increment the corresponding counter (`even_count` or `odd_count`) based on the result
    
    5. Return the result as a tuple:
        - Create a tuple with the counts of even and odd digits
        - Return the tuple
    
    Note: Be careful when handling negative numbers and converting between data types."""
    num = abs(num)
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)