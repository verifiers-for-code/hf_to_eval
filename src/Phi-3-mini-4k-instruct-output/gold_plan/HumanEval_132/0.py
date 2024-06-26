def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.
    """
    opening_brackets = []
    closing_brackets = []

    # Step 1: Initialize two empty lists to store the indices of opening and closing brackets.
    for i, char in enumerate(string):
        if char == '[':
            opening_brackets.append(i)
        elif char == ']':
            closing_brackets.append(i)

    # Step 3: Reverse the closing brackets list to match the order of nested brackets.
    closing_brackets.reverse()

    nested_brackets_counter = 0
    closing_bracket_index = 0

    # Step 5: Iterate through the opening brackets list
    for opening_bracket_index in opening_brackets:
        # Step 5a: If there are still closing brackets to check and the current opening bracket
        # index is less than the current closing bracket index:
        while closing_bracket_index < len(closing_brackets) and opening_bracket_index < closing_brackets[closing_bracket_index]:
            nested_brackets_counter += 1
            closing_bracket_index += 1

    # Step 6: Return True if the nested brackets counter is 2 or more, False otherwise.
    return nested_brackets_counter >= 2