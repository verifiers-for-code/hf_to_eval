from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats does each note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    Action Plan:
    1. Create a mapping of ASCII characters to beat counts:
        - 'o' -> 4 beats
        - 'o|' -> 2 beats
        - '.|' -> 1 beat
    
    2. Use regular expressions to find all matches of the music string against the patterns 'o', 'o|', and '.|':
        - Apply this regex search function iteratively for each musical note character in the string
    
    3. Map the matched characters to their respective beat counts using the defined mappings
    
    4. Store the beat counts in a list and return it
    
    5. Edge cases to consider:
        - Empty string
        - Strings with characters not in the provided legend
    
    6. Optimization:
        - Use a loop or generator to process each matched note rather than relying on list comprehensions or map operations for better efficiency in some scenarios
    """
    # Mapping of musical note characters to their respective beat counts
    note_to_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Initialize an empty list to store the beat counts
    beat_counts = []
    
    # Iterate over each character in the music string
    for char in music_string:
        # Check if the character is a valid musical note
        if char in note_to_beats:
            # Append the corresponding beat count to the list
            beat_counts.append(note_to_beats[char])
        else:
            # Handle the case where the character is not a valid musical note
            raise ValueError(f"Invalid musical note character: {char}")
    
    # Return the list of beat counts
    return beat_counts