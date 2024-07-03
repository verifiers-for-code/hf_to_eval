def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    

    1. Convert the input integer to a string:
       - Use the built-in str() function to convert the integer to a string
       - This allows iteration over each digit in the number
    
    2. Initialize counters for even and odd digits:
       - Create two variables, even_count and odd_count, and set them to 0
       - These counters will store the number of even and odd digits, respectively
    
    3. Iterate over each digit in the string:
       - Use a for loop to iterate over each character in the string
       - For each digit:
         a. Convert the digit back to an integer using int()
         b. Check if the digit is even or odd:
            - Use the modulus operator (%) to find the remainder of the digit divided by 2
            - If the remainder is 0, the digit is even; otherwise, it's odd
         c. Increment the appropriate counter:
            - If the digit is even, increment even_count
            - If the digit is odd, increment odd_count
    
    4. Return the counts as a tuple:
       - Use the return statement to return a tuple containing even_count and odd_count
       - The tuple will have two elements: the number of even digits and the number of odd digits
    
    Additional implementation details:
    - Ensure the function handles negative integers correctly (e.g., -12 has 2 even digits and 2 odd digits)
    - Consider adding input validation to handle non-integer inputs
    - Use descriptive variable names and comments to make the code readable and understandable"""

    # Convert the input integer to a string
    num_str = str(abs(num))

    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0

    # Iterate over each digit in the string
    for digit in num_str:
        # Convert the digit back to an integer
        digit_int = int(digit)

        # Check if the digit is even or odd
        if digit_int % 2 == 0:
            # Increment the even counter
            even_count += 1
        else:
            # Increment the odd counter
            odd_count += 1

    # Return the counts as a tuple
    return (even_count, odd_count)