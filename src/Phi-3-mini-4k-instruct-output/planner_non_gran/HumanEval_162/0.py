import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    

    Action Plan:
    1. Define the function string_to_md5 with a single parameter text.
    2. Check if the input text is an empty string:
        - If true, return None
    3. Import the hashlib module, which provides the MD5 hashing algorithm.
    4. Create an MD5 hash object using hashlib.md5().
    5. Update the hash object with the input text using the update() method.
    6. Return the hexadecimal representation of the hash using the hexdigest() method.
    7. Test the function with a sample input to ensure it works correctly."""

    if text == "":
        return None

    md5_hash = hashlib.md5()
    md5_hash.update(text.encode())
    return md5_hash.hexdigest()