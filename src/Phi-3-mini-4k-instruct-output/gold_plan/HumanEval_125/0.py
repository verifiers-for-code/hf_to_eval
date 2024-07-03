def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 

    Action Plan:
    1. Check if the input string contains any whitespace characters.
       - If yes, split the string on whitespace and return the result.

    2. If no whitespace is found, check if the string contains any commas.
       - If yes, replace commas with spaces, then split on whitespace and return the result.

    3. If neither whitespace nor commas are found:
       a. Initialize a counter for lowercase letters with odd alphabet order.
       b. Iterate through each character in the string:
          - Check if the character is lowercase.
          - If lowercase, calculate its position in the alphabet (0-25).
          - If the position is even (odd order in the alphabet), increment the counter.
       c. Return the final count.

    Note: Remember that ord('a') = 97, so you'll need to adjust the calculation to make 'a' = 0, 'b' = 1, etc.
    '''
    # Step 1: Check for whitespace
    if ' ' in txt:
        return txt.split()

    # Step 2: Check for commas
    elif ',' in txt:
        txt = txt.replace(',', ' ')
        return txt.split()

    # Step 3: Count lowercase letters with odd alphabet order
    else:
        count = 0
        for char in txt:
            if char.islower():
                # Adjust the calculation to make 'a' = 0, 'b' = 1, etc.
                if ord(char) - ord('a') % 2 == 0:
                    count += 1
        return count