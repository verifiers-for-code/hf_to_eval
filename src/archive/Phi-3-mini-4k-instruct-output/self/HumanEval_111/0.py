def histogram(test):
    # Step 1: Initialize the input string and create a list of unique letters
    letters = test.split()
    
    # Step 2: Create an empty dictionary to hold letter occurrences
    letter_counts = {}
    
    # Step 3: Iterate over each letter in the list
    for letter in letters:
        # Check if the letter is already in the dictionary; if not, add it
        if letter not in letter_counts:
            letter_counts[letter] = 1
        # Increment the letter's occurrence count
        else:
            letter_counts[letter] += 1
    
    # Step 4: Determine the maximum occurrence
    max_count = max(letter_counts.values())
    
    # Step 5: Collect the letters with max_count
    result = [letter for letter, count in letter_counts.items() if count == max_count]
    
    # Step 6: Handle edge cases
    if not test:
        return {}
    elif len(set(letters)) == 1:
        return {letters[0]: 1}
    elif len(set(letters)) == len(letters):
        return letter_counts
    else:
        return {letter: count for letter, count in letter_counts.items() if count == max_count}