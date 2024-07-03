def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Initialize an empty string variable to hold the sequence
    sequence = ""
    
    # Use a loop to iterate through each number from 0 to n (inclusive)
    for i in range(n + 1):
        # Convert the current number to a string and concatenate it with the existing sequence
        sequence += str(i) + " "
    
    # Return the final string after the loop completes
    return sequence.strip()