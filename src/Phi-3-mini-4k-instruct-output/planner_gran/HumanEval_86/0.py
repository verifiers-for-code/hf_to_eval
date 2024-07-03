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
    

    1. Split the input string into a list of words:
       - Use the appropriate string method to split the string into individual words
    
    2. Create an empty list to store the sorted words:
       - This list will hold the words with their characters sorted in ascending order
    
    3. Iterate through each word in the list of words:
       a. Convert the word to a list of characters
       b. Sort the list of characters in ascending order using the appropriate sorting method
       c. Join the sorted characters back into a string
       d. Add the sorted word to the list of sorted words
    
    4. Join the sorted words back into a single string:
       - Use a space as the separator between words
    
    5. Return the final sorted string
    
    Additional implementation details:
    - Use the `split()` method to split the input string into words
    - Use a list comprehension or a for loop to iterate through the words
    - Use the `sorted()` function to sort the characters in each word
    - Use the `join()` method to combine the sorted characters back into a string
    - Ensure that the function handles empty input strings correctly"""
    words = s.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)