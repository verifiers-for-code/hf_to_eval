from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    1. Initialize an empty list to store the prefixes
       - This list will hold all the prefixes of the input string
    
    2. Determine the length of the input string
       - Use the appropriate method to get the length of the input string
    
    3. Generate prefixes using a loop:
       a. Start a loop that iterates from 1 to the length of the input string (inclusive)
       b. In each iteration, create a prefix by concatenating the first 'i' characters of the input string
       c. Add the generated prefix to the list of prefixes
    
    4. Return the list of prefixes
       - The function should return the list of all prefixes from shortest to longest
    
    Additional implementation details:
    - Use a for loop or a while loop to iterate from 1 to the length of the input string
    - Use string slicing to extract the first 'i' characters of the input string
    - Use the append method to add each prefix to the list
    - Ensure the function handles empty input strings correctly
    - Consider using a list comprehension as an alternative to the loop
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes