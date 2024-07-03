def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    # Initialize an empty list to store prime numbers
    primes = []

    # Iterate through numbers from 2 to n-1 (inclusive)
    for num in range(2, n):
        # Assume the current number is prime initially
        is_prime = True

        # Check if the current number is prime
        for i in range(2, num):
            # If the current number is divisible by any number in the range, it's not prime
            if num % i == 0:
                is_prime = False
                break

        # If the number is still considered prime after all checks, add it to the prime numbers list
        if is_prime:
            primes.append(num)

    # Return the list of prime numbers
    return primes