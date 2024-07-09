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
    1. Define a helper function `is_palindrome` to check if a number is a palindrome:
        - Convert the number to a string
        - Compare the string with its reverse
        - Return `True` if they are equal, `False` otherwise
    
    2. Initialize two counters, `even_palindromes` and `odd_palindromes`, to store the counts of even and odd palindromes respectively
    
    3. Iterate over the range(1, n) using a for loop:
        - For each number `i` in the range:
            a. Check if `i` is a palindrome using the `is_palindrome` function
            b. If `i` is a palindrome:
                - If `i` is even, increment `even_palindromes`
                - If `i` is odd, increment `odd_palindromes`
    
    4. After the loop, return a tuple containing `even_palindromes` and `odd_palindromes`
    
    Note: Use the `is_palindrome` function to efficiently check for palindromes.
    Be careful when iterating over the range and updating the counters.
    """
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return (even_palindromes, odd_palindromes)