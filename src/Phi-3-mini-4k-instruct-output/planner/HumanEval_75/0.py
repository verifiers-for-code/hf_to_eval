def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    

    Action Plan:
    1. Define a function `is_multiply_prime` that takes an integer `a` as input.
    2. Create a helper function `is_prime` to check if a number is prime:
        a. Iterate from 2 to the square root of the number.
        b. Check if the number is divisible by any of these values.
        c. Return `True` if the number is prime, `False` otherwise.
    3. Implement the logic to check if `a` is the multiplication of 3 prime numbers:
        a. Initialize a counter to 0.
        b. Iterate from 2 to the square root of `a`.
        c. For each number, check if it is prime using the `is_prime` function.
        d. If the number is prime, divide `a` by the number and increment the counter.
        e. If the counter reaches 3, return `True`.
        f. If the loop completes without finding 3 prime factors, return `False`.
    4. Handle the example case: `is_multiply_prime(30)` should return `True`.
    5. Consider edge cases, such as `a` being less than 100, and handle them accordingly."""

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if a < 100:
        factors = []
        for i in range(2, int(a**0.5) + 1):
            if is_prime(i) and a % i == 0:
                factors.append(i)
                a //= i
                if len(factors) == 3:
                    return True
        return False

    return False