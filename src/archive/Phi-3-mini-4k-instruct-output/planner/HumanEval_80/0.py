def is_happy(s):
    """
    You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string is happy, False otherwise.
    """
    # Step 2: Check if the length of the string s is less than 3
    if len(s) < 3:
        return False

    # Step 3: Iterate through the string s in chunks of 3 characters
    for i in range(len(s) - 2):
        chunk = s[i:i+3]

        # Step 3.1: Check if all characters in the chunk are distinct
        if len(chunk) != len(set(chunk)):
            return False

    # Step 4: If the loop completes without returning False, return True
    return True