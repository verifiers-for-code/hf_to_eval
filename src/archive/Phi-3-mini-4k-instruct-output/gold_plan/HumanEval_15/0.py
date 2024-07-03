def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Step 1: Create a sequence of numbers from 0 to n (inclusive)
    num_sequence = list(range(n + 1))

    # Step 2: Convert each number in the sequence to a string
    str_sequence = [str(num) for num in num_sequence]

    # Step 3: Join the string representations
    result = ' '.join(str_sequence)

    # Step 4: Return the resulting string
    return result