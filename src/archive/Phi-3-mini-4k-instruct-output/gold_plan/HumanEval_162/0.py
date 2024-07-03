import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    Action Plan:
    1. Import the necessary module for MD5 hashing (hint: look into the 'hashlib' module)
    2. Check if the input 'text' is an empty string
       - If it is, return None immediately
    3. If 'text' is not empty:
       a. Convert the input string to bytes (consider using encode method with 'ascii' encoding)
       b. Create an MD5 hash object
       c. Update the hash object with the bytes from step 3a
       d. Generate the hexadecimal representation of the hash (look for a method that returns a string)
    4. Return the resulting hash string
    """
    if not text:
        return None

    text_bytes = text.encode('ascii')
    md5_hash = hashlib.md5()
    md5_hash.update(text_bytes)
    return md5_hash.hexdigest()