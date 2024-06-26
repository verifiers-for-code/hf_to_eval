def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    result = ""
    vowels = set("aeiouAEIOU")

    for char in text:
        if char not in vowels:
            result += char

    return result