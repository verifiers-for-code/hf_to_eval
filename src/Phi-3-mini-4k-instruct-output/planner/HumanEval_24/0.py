def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    

    Action Plan:
    1. Understand the problem: Find the largest number that divides a given number n evenly, smaller than n.
    2. Initialize a variable, largest_divisor, to store the largest divisor. Set it to 1, as 1 is a divisor of all numbers.
    3. Implement a loop that starts from 2 (the smallest possible divisor) and goes up to n-1 (the largest possible divisor).
    4. Inside the loop:
        a. Check if the current number is a divisor of n by using the modulus operator (%).
        b. If it is a divisor, update largest_divisor to the current number.
    5. After the loop, return the largest_divisor as the result.
    
    Note: Be careful with the loop range to ensure it covers all possible divisors."""
    largest_divisor = 1
    for i in range(2, n):
        if n % i == 0:
            largest_divisor = i
    return largest_divisor