def hex_key(num):
    """
    You have been tasked to write a function that receives a hexadecimal number as a string and counts the number of hexadecimal digits that are primes.
    
    Parameters:
    num (str): A hexadecimal number as a string.
    
    Returns:
    int: The count of hexadecimal digits that are primes.
    
    Action Plan:
    1. Define a list of prime numbers to check for (2, 3, 5, 7, B, D).
    2. Convert the input hexadecimal string to a list of characters.
    3. Initialize a counter variable to store the count of prime digits.
    4. Iterate through each character in the list:
        a. Check if the character is a prime number (using the defined list).
        b. If the character is a prime number, increment the counter.
    5. After iterating through all characters, return the final count of prime digits.
    6. Consider handling potential edge cases, such as an empty input string.
    """
    # Step 1: Define a list of prime numbers to check for
    primes = [2, 3, 5, 7, 'B', 'D']
    
    # Step 2: Convert the input hexadecimal string to a list of characters
    hex_chars = list(num)
    
    # Step 3: Initialize a counter variable to store the count of prime digits
    prime_count = 0
    
    # Step 4: Iterate through each character in the list
    for char in hex_chars:
        # Step 4a: Check if the character is a prime number
        if char in primes:
            # Step 4b: Increment the counter if the character is a prime number
            prime_count += 1
    
    # Step 5: Return the final count of prime digits
    return prime_count