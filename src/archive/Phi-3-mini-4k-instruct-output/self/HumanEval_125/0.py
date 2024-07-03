def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Check if the input string contains whitespace
    if ' ' in txt:
        return txt.split(' ')
    # Check if the input string contains comma
    elif ',' in txt:
        return txt.split(',')
    # If neither whitespace nor comma is found, count the number of lower-case letters with odd order in the alphabet
    else:
        count = sum(1 for char in txt.lower() if ord(char) % 2 != 0 and 'a' <= char <= 'z')
        return count