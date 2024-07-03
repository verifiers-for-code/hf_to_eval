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
    1. Define a helper function is_palindrome that takes an integer as input and returns True if it's a palindrome, False otherwise.
    2. Initialize two counters, even_palindrome_count and odd_palindrome_count, to store the number of even and odd palindromes, respectively.
    3. Iterate through the range of numbers from 1 to n (inclusive):
       a. Check if the current number is a palindrome using the helper function.
       b. If it's a palindrome, check its parity (even or odd).
       c. Increment the corresponding counter (even_palindrome_count or odd_palindrome_count).
    4. After iterating through the entire range, return a tuple containing the even_palindrome_count and odd_palindrome_count.
    """
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)