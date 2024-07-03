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
    # Step 1: Check if the input string contains any whitespace characters.
    if any(char.isspace() for char in txt):
        return txt.split()

    # Step 2: If no whitespace is found, check if the string contains any commas.
    elif ',' in txt:
        txt = txt.replace(',', ' ')
        return txt.split()

    # Step 3: If neither whitespace nor commas are found:
    else:
        count = 0
        for char in txt:
            # Check if the character is lowercase.
            if char.islower():
                # Calculate its position in the alphabet (0-25).
                char_ord = ord(char) - ord('a')
                # If the position is even (odd order in the alphabet), increment the counter.
                if char_ord % 2 != 0:
                    count += 1
        return count