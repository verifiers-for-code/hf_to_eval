def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    

    Action Plan:
    1. Ensure `a` and `b` are positive integers; handle error if not
    2. Generate a list of integers from `a` to `b` (inclusive)
    3. Create a helper function to extract and filter even digits:
        a. Convert a number to a string to iterate over its digits
        b. Check if each digit is even
        c. Return the even digits as a list
    
    4. Apply the helper function to each integer in the list:
        a. Use list comprehension for concise implementation
    
    5. Remove odd digits and sort the remaining list
    6. Test with the provided example and edge cases, ensuring ascending order and only even digits
    7. Optimize for readability and performance
    """
    # Ensure a and b are positive integers
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers")

    # Generate a list of integers from a to b (inclusive)
    numbers = list(range(a, b + 1))

    # Helper function to extract and filter even digits
    def extract_even_digits(num):
        return [int(digit) for digit in str(num) if int(digit) % 2 == 0]

    # Apply the helper function to each integer in the list
    even_digits = [digit for num in numbers for digit in extract_even_digits(num)]

    # Remove odd digits and sort the remaining list
    even_digits_sorted = sorted(set(even_digits))

    return even_digits_sorted