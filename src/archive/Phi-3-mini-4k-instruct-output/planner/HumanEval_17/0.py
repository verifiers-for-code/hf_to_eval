from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    
    Action Plan:
    1. Define a dictionary to map note symbols ('o', 'o|', '.|') to their corresponding beats (4, 2, 1).
    2. Split the input string into a list of individual notes using the space character as a delimiter.
    3. Initialize an empty list to store the beats.
    4. Iterate through each note in the list of notes:
        a. Check if the note is in the dictionary.
        b. If it is, append the corresponding beat to the list of beats.
        c. If it's not, raise a ValueError indicating an invalid note.
    5. Return the list of beats.
    
    Note: Be careful to handle the case where a note is not in the dictionary.
    Use the dictionary to efficiently map note symbols to their corresponding beats."""
    
    note_to_beat = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    beats = []
    
    for note in notes:
        if note in note_to_beat:
            beats.append(note_to_beat[note])
        else:
            raise ValueError(f"Invalid note: {note}")
    
    return beats