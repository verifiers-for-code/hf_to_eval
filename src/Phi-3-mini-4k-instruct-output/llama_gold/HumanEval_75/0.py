def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    

    Action Plan:
    1. Define a helper function `is_prime(n)` to check if a number `n` is prime:
       a. Iterate from 2 to `n-1` and check if `n` is divisible by any of these numbers.
       b. If `n` is divisible, return `False`.
       c. If `n` is not divisible by any of these numbers, return `True`.
    2. Initialize a loop to iterate through all possible combinations of three prime numbers `i`, `j`, and `k` between 2 and 100.
    3. For each combination:
       a. Check if `i`, `j`, and `k` are prime using the `is_prime` function.
       b. If all three are prime, calculate their product.
       c. If the product equals the input number `a`, return `True`.
    4. If no combination of three prime numbers multiplies to `a`, return `False`."""

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(i, 101):
            if not is_prime(j):
                continue
            for k in range(j, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False