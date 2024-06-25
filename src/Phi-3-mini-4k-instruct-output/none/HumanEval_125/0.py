def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    # Check if the input string contains only lower-case letters
    if txt.islower():
        # Count the number of lower-case letters with odd order in the alphabet
        odd_letters_count = sum(1 for char in txt if ord(char) % 2 != 0)
        return odd_letters_count
    else:
        # Split the string on whitespace or commas
        words = txt.split()
        if len(words) == 1 and ',' in words[0]:
            words = words[0].split(',')
        return words