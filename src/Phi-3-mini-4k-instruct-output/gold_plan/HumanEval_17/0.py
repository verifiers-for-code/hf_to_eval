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
    1. Create a dictionary to map note symbols to their durations:
       - 'o' maps to 4
       - 'o|' maps to 2
       - '.|' maps to 1

    2. Split the input string into individual notes using the space character as a delimiter.

    3. Iterate through the split notes:
       - For each note, look up its duration in the mapping dictionary
       - Add the duration to the result list

    4. Ensure to handle any potential empty strings resulting from the split operation by filtering them out.

    5. Return the list of durations.
    """
    note_durations = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    durations = [note_durations[note] for note in notes if note in note_durations]
    return durations