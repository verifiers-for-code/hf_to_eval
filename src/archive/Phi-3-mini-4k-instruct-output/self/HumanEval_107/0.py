def is_palindrome(n):
    """
    Helper function to check if a number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_count = 0
    odd_count = 0

    # Loop through the range(1, n+1)
    for i in range(1, n+1):
        # Check if the number is a palindrome
        if is_palindrome(i):
            # Increment the appropriate counter based on the number's parity
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)