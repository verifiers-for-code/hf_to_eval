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
    1. Initialize an empty list to store prime numbers.
    2. Iterate through the range of numbers from 2 to n-1 (exclusive):
       a. For each number, initialize a flag to assume it's prime (True).
       b. Check if the number is divisible by any number from 2 to the number itself (exclusive).
       c. If it's divisible, set the prime flag to False and break the inner loop.
       d. If the prime flag remains True, add the number to the list of prime numbers.
    3. Return the list of prime numbers."""
    
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes