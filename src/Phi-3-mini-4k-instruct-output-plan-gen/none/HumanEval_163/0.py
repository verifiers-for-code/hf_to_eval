
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []

    # Iterate through the range of numbers between a and b
    for num in range(a, b+1):
        # Convert the number to a string to iterate through its digits
        num_str = str(num)
        for digit in num_str:
            # Check if the digit is even
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Sort the even digits in ascending order
    even_digits.sort()

    return even_digits