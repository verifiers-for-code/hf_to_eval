def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.

    Action Plan:
    1. Define a helper function 'is_palindrome(num)' to check if a number is a palindrome:
       - Convert the number to a string
       - Check if the string reads the same forwards and backwards
    
    2. Initialize two variables to count even and odd palindromes

    3. Iterate through numbers from 1 to n (inclusive):
       - Check if the current number is a palindrome using the helper function
       - If it's a palindrome:
         - Check if it's even or odd
         - Increment the appropriate counter

    4. Return a tuple containing the counts of even and odd palindromes
    """

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)