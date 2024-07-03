def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    

    Action Plan:
    1. Understand the problem:
        - The function should return a string containing space-delimited numbers from 0 to n (inclusive).
    
    2. Generate the sequence of numbers:
        - Use a loop to iterate from 0 to n (inclusive).
        - In each iteration, generate the current number.
    
    3. Convert the sequence to a string:
        - Use a list comprehension or a loop to convert each number to a string.
    
    4. Join the numbers with spaces:
        - Use the `join()` method to concatenate the strings with spaces in between.
    
    5. Return the final result:
        - Return the resulting string containing the space-delimited numbers.
    
    Note: Consider using a list comprehension or a loop to generate the sequence of numbers.
    Be careful when converting numbers to strings and joining them with spaces."""
    
    # Generate the sequence of numbers
    numbers = [str(i) for i in range(n+1)]
    
    # Join the numbers with spaces
    result = ' '.join(numbers)
    
    # Return the final result
    return result