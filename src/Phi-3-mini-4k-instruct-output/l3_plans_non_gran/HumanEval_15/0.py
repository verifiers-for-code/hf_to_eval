def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    

    Action Plan:
    1. Define the function string_sequence with a single parameter n, an integer.
    2. Initialize an empty list or variable to store the sequence of numbers.
    3. Use a loop or list comprehension to generate the sequence of numbers from 0 to n (inclusive).
    4. Convert the sequence into a string, using a separator (e.g., space) to separate the numbers.
    5. Use the join() method to concatenate the sequence into a single string, with spaces between each number.
    6. Return the resulting string."""
    
    # Step 2: Initialize an empty list to store the sequence of numbers
    sequence = []
    
    # Step 3: Generate the sequence of numbers from 0 to n (inclusive)
    for i in range(n+1):
        sequence.append(str(i))
    
    # Step 4: Convert the sequence into a string, using a separator (e.g., space) to separate the numbers
    sequence_str = ' '.join(sequence)
    
    # Step 6: Return the resulting string
    return sequence_str