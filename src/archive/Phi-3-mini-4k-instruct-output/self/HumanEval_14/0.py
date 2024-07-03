from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
    Action Plan:
    1. Initialize an empty list to store prefixes
    2. Implement a loop that iterates from 1 to the length of the input string
        - For each iteration, create a substring using the loop counter (starting index)
        - Add the substring to the list of prefixes
    3. After the loop, return the list of prefixes
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes