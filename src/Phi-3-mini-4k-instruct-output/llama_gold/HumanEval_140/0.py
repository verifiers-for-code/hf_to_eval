def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    

    Action Plan:
    1. Initialize an empty string to store the modified text.
    2. Initialize counters to track the start and end positions of consecutive spaces.
    3. Iterate through each character in the input text:
       a. If the character is a space:
          - Increment the end counter
       b. If the character is not a space:
          - Check the number of consecutive spaces:
             i. If there are more than 2 consecutive spaces:
                - Add a '-' character to the modified string
             ii. If there are 1 or 2 consecutive spaces:
                - Add the corresponding number of '_' characters to the modified string
          - Add the current character to the modified string
          - Update the start and end counters
    4. After iterating through the entire string:
       a. Check if there are trailing spaces:
          - If there are more than 2 trailing spaces:
             - Add a '-' character to the modified string
          - If there are 1 or 2 trailing spaces:
             - Add the corresponding number of '_' characters to the modified string
    5. Return the modified string with replaced spaces.
    """
    modified_text = ""
    start_space_count = 0
    end_space_count = 0

    for char in text:
        if char == " ":
            end_space_count += 1
        else:
            if end_space_count > 2:
                modified_text += "-"
            elif end_space_count > 0:
                modified_text += "_" * end_space_count
            modified_text += char
            start_space_count = 0
            end_space_count = 0

    if end_space_count > 2:
        modified_text += "-"
    elif end_space_count > 0:
        modified_text += "_" * end_space_count

    return modified_text