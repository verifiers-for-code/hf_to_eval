def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3

    Action Plan:
    1. Define a string containing all vowels (both lowercase and uppercase).
    2. Initialize a counter for vowels.
    3. Iterate through each character in the input string:
       - If the character is in the vowels string, increment the counter.
    4. After the loop, check if the last character of the input string is 'y' or 'Y':
       - If so, increment the counter by 1.
    5. Return the final vowel count.

    Additional test cases:
    >>> vowels_count("python")
    2
    >>> vowels_count("RHYTHM")
    1
    >>> vowels_count("aEiOu")
    5
    >>> vowels_count("xyx")
    1
    >>> vowels_count("Y")
    1
    >>> vowels_count("")
    0
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    if s.endswith("y"):
        count += 1
    return count