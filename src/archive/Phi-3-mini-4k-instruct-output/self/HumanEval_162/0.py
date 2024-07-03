import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    True

    Action Plan:
    1. Import the hashlib library which contains the MD5 function:
        - hashlib.md5()
    
    2. Handle the empty string case in the function:
        - If the input string is empty, return None
    
    3. Generate the MD5 hash:
        - Convert the input string to bytes
        - Use hashlib.md5() to compute the MD5 hash
        - Convert the hash object to a hexadecimal string
    
    4. Return the result:
        - Return the hexadecimal string representing the MD5 hash of the input string
    """
    if not text:
        return None

    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()