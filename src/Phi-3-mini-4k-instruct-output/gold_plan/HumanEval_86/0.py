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
    1. Split the input string 's' into words using the space character as a delimiter.
    2. For each word in the split result:
       a. Convert the word into a list of characters.
       b. Sort this list of characters in ascending order.
       c. Join the sorted characters back into a string.
    3. Join all the processed words back together with spaces between them.
    4. Return the final joined string.

    Hint: You can use string methods like split() and join(), and the sorted() function
    to accomplish these tasks efficiently.
    """
    # Step 1: Split the input string 's' into words using the space character as a delimiter.
    words = s.split(' ')

    # Step 2: For each word in the split result:
    # a. Convert the word into a list of characters.
    # b. Sort this list of characters in ascending order.
    # c. Join the sorted characters back into a string.
    ordered_words = [''.join(sorted(word)) for word in words]

    # Step 3: Join all the processed words back together with spaces between them.
    ordered_string = ' '.join(ordered_words)

    # Step 4: Return the final joined string.
    return ordered_string