def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Step 1: Initialize an empty string variable to hold the sequence
    sequence = ""

    # Step 2: Use a loop to iterate through each number from 0 to n (inclusive)
    for num in range(n + 1):
        # Step 3: In each iteration, convert the current number to a string and concatenate it with the existing sequence
        sequence += str(num) + " "

    # Step 4: Return the final string after the loop completes
    return sequence.strip()  # Remove the trailing space