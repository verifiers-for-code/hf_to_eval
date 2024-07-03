from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Step 1: Initialize an empty list to store the prefixes.
    prefixes = []

    # Step 2: Iterate through the input string
    for i in range(len(string)):
        # For each iteration, consider the characters from the start of the string up to the current position.
        # Create a prefix by slicing the string from the start to the current position (inclusive).
        prefix = string[:i+1]
        # Add this prefix to the list of prefixes.
        prefixes.append(prefix)

    # Step 3: After the iteration is complete, return the list of prefixes.
    return prefixes