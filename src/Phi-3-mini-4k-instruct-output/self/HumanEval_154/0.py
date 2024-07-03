def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    
    Action Plan:
    1. Define the check_rotation() helper function to rotate a word:
        - Implement rotations by slicing and concatenating strings
    
    2. In the main cycpattern_check function:
        a. Handle edge cases:
            - Return False if either word is empty
            - Return False if lengths differ by more than 1 (as one rotation cannot match)
        
        b. Iterate through each position in the first word:
            - For each position, rotate the second word
            - Check if the rotated word is a substring of the first word
        
        c. Return True if any rotation is a substring, else return False after completing the iteration"""
    
    def check_rotation(word, rotation):
        """Helper function to rotate a word by slicing and concatenating strings."""
        return word[rotation:] + word[:rotation]
    
    # Handle edge cases
    if not a or not b or abs(len(a) - len(b)) > 1:
        return False
    
    # Iterate through each position in the first word
    for i in range(len(a) - len(b) + 1):
        # Rotate the second word
        rotated_word = check_rotation(b, i)
        # Check if the rotated word is a substring of the first word
        if rotated_word in a:
            return True
    
    # Return False if no rotation is a substring
    return False