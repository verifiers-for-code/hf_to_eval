def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if the number is less than 100
    if a < 100:
        # Initialize a list to store the prime factors
        prime_factors = []
        # Iterate over the numbers from 2 to the given number
        for i in range(2, a + 1):
            # Check if the current number is a prime factor
            if a % i == 0:
                # Check if the current number is a prime number
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    # Add the prime factor to the list
                    prime_factors.append(i)
        # Check if the list has exactly 3 prime factors
        if len(prime_factors) == 3:
            return True
    return False