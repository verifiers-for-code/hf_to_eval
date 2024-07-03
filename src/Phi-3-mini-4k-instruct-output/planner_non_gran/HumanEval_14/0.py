from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    

    Action Plan:
    1. Define a function `all_prefixes` that takes a string as input.
    2. Initialize an empty list `prefixes` to store the prefixes.
    3. Iterate through the input string using a loop:
        a. For each character in the string, create a new prefix by concatenating the character with the previous prefixes.
        b. Add the new prefix to the `prefixes` list.
    4. After the loop, return the `prefixes` list.
    5. Consider using a more efficient approach, such as using a generator expression or a list comprehension, to generate the prefixes.
    
    Note: The problem statement specifies that the output should be a list of all prefixes from shortest to longest. Ensure that the implementation follows this requirement."""
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes