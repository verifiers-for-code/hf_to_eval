def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    :param txt: A string to be checked
    :return: True if the last character is an alphabetical character and is not a part of a word, False otherwise

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False
    """
    # Split the string into words
    words = txt.split()

    # Check if the string is empty
    if not txt:
        return False

    # Get the last word
    last_word = words[-1]

    # Check if the last character of the last word is an alphabetical character
    if last_word and last_word[-1].isalpha():
        return False
    else:
        return True