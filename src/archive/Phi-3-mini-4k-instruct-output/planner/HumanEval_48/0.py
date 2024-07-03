def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
    text (str): The input string to check for palindrome.
    
    Returns:
    bool: True if the input string is a palindrome, False otherwise.
    
    Action Plan:
    1. Define the function is_palindrome with a string parameter text.
    2. Preprocess the input string:
        a. Convert the string to lowercase to ignore case sensitivity.
        b. Remove any non-alphanumeric characters (e.g., spaces, punctuation) to focus on the alphanumeric content.
    3. Implement the palindrome check logic:
        a. Compare the preprocessed string with its reverse.
        b. If the string is equal to its reverse, return True (indicating a palindrome).
        c. If the string is not equal to its reverse, return False (indicating not a palindrome).
    4. Return the result of the palindrome check.
    """
    # Preprocess the input string
    preprocessed_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the preprocessed string is a palindrome
    return preprocessed_text == preprocessed_text[::-1]