def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 

    Action Plan:
    1. Handle the edge case: If the input string is empty, return False.
    2. Split the input string into words using space as the delimiter.
    3. Extract the last element from the split result.
    4. Check if the last element is a single character:
       - If it's not a single character, return False.
    5. If it is a single character, check if it's a letter:
       - You can use ASCII values or a built-in method to check if it's a letter.
       - Make sure to consider both uppercase and lowercase letters.
    6. Return True if it's a letter, False otherwise.
    '''
    if not txt:
        return False

    words = txt.split(' ')
    last_word = words[-1]

    if len(last_word) != 1:
        return False

    last_char = last_word[0]
    if last_char.isalpha():
        return True
    else:
        return False