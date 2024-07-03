from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    

    Action Plan:
    1. Create a dictionary to map each note symbol to its corresponding number of beats.
    2. Split the input music string into a list of individual notes, using spaces as separators.
    3. Initialize an empty list to store the beats for each note.
    4. Iterate through each note in the list:
       a. Look up the note in the mapping dictionary.
       b. Append the corresponding number of beats to the result list.
    5. Return the list of beats, where each element represents the duration of a note in the input music string."""

    # Step 1: Create a dictionary to map each note symbol to its corresponding number of beats.
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Step 2: Split the input music string into a list of individual notes, using spaces as separators.
    notes = music_string.split()

    # Step 3: Initialize an empty list to store the beats for each note.
    beats = []

    # Step 4: Iterate through each note in the list:
    for note in notes:
        # Step 4a: Look up the note in the mapping dictionary.
        beats.append(note_to_beats[note])

    # Step 5: Return the list of beats.
    return beats