import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Step 1: Create a mapping of ASCII characters to beat counts
    beat_mapping = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Step 2: Use regular expressions to find all matches of the music string against the patterns 'o', 'o|', and '.|'
    notes = re.findall(r'[o|.]', music_string)

    # Step 3: Map the matched characters to their respective beat counts using the defined mappings
    beats = [beat_mapping[note] for note in notes]

    # Step 4: Return the list of beat counts
    return beats