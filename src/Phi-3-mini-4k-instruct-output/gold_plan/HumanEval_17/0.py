from typing import List

def parse_music(music_string: str) -> List[int]:
    # Step 1: Create a dictionary to map note symbols to their durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Step 2: Split the input string into individual notes using the space character as a delimiter
    notes = music_string.split()

    # Step 3: Iterate through the split notes
    durations = []
    for note in notes:
        # Step 3.1: Look up the duration of the note in the mapping dictionary
        duration = note_durations.get(note, 0)

        # Step 3.2: Add the duration to the result list
        durations.append(duration)

    # Step 4: Filter out any potential empty strings resulting from the split operation
    durations = [duration for duration in durations if duration != 0]

    # Step 5: Return the list of durations
    return durations