def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    

    Action Plan:
    1. Split the input string into a list of words using space as the separator.
    2. Initialize an empty list to store the processed words.
    3. Iterate through each word in the list:
       a. Convert the word into a list of characters.
       b. Sort the list of characters in ascending order based on ASCII value.
       c. Join the sorted characters back into a string.
       d. Add the processed word to the result list.
    4. Join the processed words back into a single string using space as the separator.
    5. Return the resulting string with words in ascending order of characters."""

    words = s.split()
    processed_words = []

    for word in words:
        sorted_word = ''.join(sorted(word))
        processed_words.append(sorted_word)

    return ' '.join(processed_words)