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
    1. Check if n is less than or equal to 0:
        - If true, return an empty array
    
    2. Initialize an empty array to store the prime numbers (result)
    3. Initialize a flag (is_prime) to True, assuming the first number (2) is prime
    4. Iterate through numbers from 2 to n (inclusive):
        a. For each number, check if it's prime:
            - Iterate from 2 to the square root of the number
            - If the number is divisible by any of these values, set the is_prime flag to False
        b. If the number is prime (is_prime flag is True):
            - Append the number to the result array
            - Set the is_prime flag to False
    5. Return the result array containing the first n prime numbers less than n
    
    Note: Optimize the prime number check by only iterating up to the square root of the number.
    Be careful with the iteration range and the logic for finding prime numbers."""
    
    if n <= 0:
        return []
    
    result = []
    is_prime = True
    
    for num in range(2, n):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
            is_prime = False
    
    return result