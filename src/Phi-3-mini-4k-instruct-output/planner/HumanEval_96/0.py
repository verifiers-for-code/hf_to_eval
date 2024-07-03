def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    

    Action Plan:
    1. Define a helper function `is_prime(num)` to check if a number is prime:
        a. Handle edge cases (e.g., 0 and 1 are not prime)
        b. Iterate from 2 to the square root of the number (inclusive)
        c. Check if the number is divisible by any of these values
        d. Return `True` if the number is prime, `False` otherwise
    
    2. Define the main function `count_up_to(n)`:
        a. Initialize an empty list `primes` to store the prime numbers
        b. Iterate from 2 to `n` (inclusive)
        c. For each number, check if it is prime using the `is_prime` function
        d. If the number is prime, add it to the `primes` list
    
    3. After the iteration, return the `primes` list
    
    Note: Use appropriate data structures and control structures to implement the solution efficiently.
    Be careful with the prime number checking logic to ensure correctness."""
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes