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
    1. Split the input string into a list of words using the split() method.
    2. Create an empty list to store the sorted words.
    3. Iterate through each word in the list of words:
        a. Convert the word to a list of characters using the list() function.
        b. Sort the list of characters in ascending order based on their ASCII values using the sorted() function.
        c. Join the sorted characters back into a single string using the join() method.
        d. Add the sorted word to the list of sorted words.
    4. Join the list of sorted words back into a single string using the join() method, with spaces in between.
    5. Return the resulting string, which is the anti-shuffled version of the input string.
    
    Note: Use appropriate string and list methods for splitting, sorting, and joining.
    Be careful to preserve the original word order and spacing."""
    
    words = s.split()
    sorted_words = []
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        sorted_words.append(sorted_word)
    return ' '.join(sorted_words)