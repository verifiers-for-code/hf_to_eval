import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    

    Action Plan:
    1. Check if the input string 'text' is empty:
        - If empty, return None
    2. Import the necessary module for MD5 hashing (hashlib)
    3. Create an MD5 hash object using hashlib.md5()
    4. Update the MD5 hash object with the input string 'text' using the update() method
    5. Retrieve the MD5 hash equivalent string using the hexdigest() method
    6. Return the MD5 hash equivalent string
    
    Note: Ensure you have the necessary library (hashlib) installed and imported correctly.
    Be aware of the encoding of the input string, as it may affect the MD5 hashing result."""
    
    if not text:
        return None
    
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()