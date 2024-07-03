from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    

    1. Initialize an empty list to store the beats
       - This list will hold the integer values representing the beats of each note
    
    2. Iterate through each character in the input string:
       a. Check if the character is a letter (a-z)
       b. If it's a letter, determine the note type:
          - If it's 'o', it's a whole note (4 beats)
          - If it's 'o|', it's a half note (2 beats)
          - If it's '.|', it's a quarter note (1 beat)
       c. If it's not a letter, it's not a valid note, so skip it
       d. Add the corresponding number of beats to the beats list
    
    3. Return the list of beats
    
    Additional implementation details:
    - Use a loop to iterate through each character in the input string
    - Use the `isalpha()` method to check if a character is a letter
    - Use the `ord()` function to get the ASCII value of a character and determine its corresponding note type
    - Use a conditional statement (if-elif-else) to handle different note types
    - Use the `append()` method to add beats to the list
    - Ensure the function handles empty input strings correctly
    """
    beats = []
    for char in music_string:
        if char.isalpha():
            if char == 'o':
                beats.append(4)
            elif char == 'o|':
                beats.append(2)
            elif char == '.|':
                beats.append(1)
    return beats