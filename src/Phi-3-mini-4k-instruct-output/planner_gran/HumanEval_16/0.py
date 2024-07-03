def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    1. Initialize an empty set to store distinct characters
       - A set automatically removes duplicates, making it ideal for counting unique characters
    
    2. Convert the input string to lowercase for case-insensitive comparison
       - Use the appropriate string method to convert the string to lowercase
    
    3. Iterate through each character in the lowercase string:
       a. Add the character to the set of distinct characters
       - Since sets automatically remove duplicates, this will ensure only unique characters are counted
    
    4. Return the count of distinct characters
       - Use the appropriate method to get the length of the set
    
    Additional implementation details:
    - Use a set to store distinct characters, as it automatically removes duplicates
    - Convert the input string to lowercase to ensure case-insensitive comparison
    - Iterate through each character in the string, adding it to the set
    - Use the len() function to get the count of distinct characters
    - Ensure the function handles empty input strings correctly
    """
    distinct_characters = set()
    lowercase_string = string.lower()
    
    for char in lowercase_string:
        distinct_characters.add(char)
    
    return len(distinct_characters)