
def histogram(test):
    # Check if the input string is empty
    if not test:
        return {}

    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate through the string and count the occurrences of each letter
    for letter in test:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Find the maximum count
    max_count = max(letter_count.values())

    # Create a list to store the letters with the maximum count
    max_letters = [letter for letter, count in letter_count.items() if count == max_count]

    # Return the dictionary of letters with the maximum count
    return dict(zip(max_letters, [max_count] * len(max_letters)))