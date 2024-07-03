import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    

    1. Check if the input string is empty:
       - Use a conditional statement to check if the input string is empty
       - If empty, return None immediately
    
    2. Calculate the MD5 hash of the input string:
       - Import the hashlib library, which provides the MD5 hashing functionality
       - Create an MD5 hash object using the input string
       - Update the hash object with the input string
       - Get the hexadecimal digest of the hash object
    
    3. Convert the MD5 hash to a hexadecimal string:
       - Use the hexdigest() method of the hash object to get the hexadecimal representation of the hash
       - This will be a string of 32 characters, representing the MD5 hash
    
    4. Return the MD5 hash string:
       - Return the calculated MD5 hash as a string
    
    Additional implementation details:
    - Use the appropriate library (hashlib) to calculate the MD5 hash
    - Ensure the function handles empty input strings correctly by returning None
    - Use the correct method to get the hexadecimal representation of the hash (hexdigest())
    - Test the function with sample inputs to verify its correctness"""
    if not text:
        return None
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()