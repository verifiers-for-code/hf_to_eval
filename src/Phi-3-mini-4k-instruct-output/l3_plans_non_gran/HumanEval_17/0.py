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
    1. Define the function `parse_music` with a single parameter `music_string` of type `str`.
    2. Create a dictionary `note_to_beat` to map musical notes to their corresponding beat lengths.
        - Add entries for 'o', 'o|', '.|', and other possible musical notes (if needed).
        - Set the beat length for each note (e.g., 4 for 'o', 2 for 'o|', 1 for '.|', etc.).
    3. Initialize an empty list `beat_lengths` to store the parsed beat lengths.
    4. Iterate through each character `note` in the input `music_string`:
        - Convert the note to lowercase to handle case-insensitive matching.
        - Check if the note exists in the `note_to_beat` dictionary.
        - If it does, append the corresponding beat length to the `beat_lengths` list.
    5. Return the `beat_lengths` list.
    
    Note: Be careful when handling edge cases, such as invalid musical notes or empty input strings.
    Consider adding error handling or input validation if necessary."""

    note_to_beat = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    beat_lengths = []

    for note in music_string.split():
        note = note.lower()
        if note in note_to_beat:
            beat_lengths.append(note_to_beat[note])
        else:
            raise ValueError(f"Invalid musical note: {note}")

    return beat_lengths