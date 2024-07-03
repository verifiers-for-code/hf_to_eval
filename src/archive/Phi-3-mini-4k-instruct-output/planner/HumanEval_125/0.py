def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    
    Parameters:
    txt (str): Input string
    
    Returns:
    list: List of words split on whitespace or number of lower-case letters with odd order in the alphabet
    """
    # Check if the input string contains whitespace
    if ' ' in txt:
        return txt.split(' ')
    # Check if the input string contains comma
    elif ',' in txt:
        return txt.split(',')
    else:
        # Count the number of lower-case letters with odd order in the alphabet
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count