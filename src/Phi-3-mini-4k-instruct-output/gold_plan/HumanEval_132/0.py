def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True

    Action Plan:
    1. Initialize two empty lists to store the indices of opening and closing brackets.
    2. Iterate through the input string:
       a. If the character is '[', add its index to the opening brackets list.
       b. If the character is ']', add its index to the closing brackets list.
    3. Reverse the closing brackets list to match the order of nested brackets.
    4. Initialize a counter for nested brackets and an index for closing brackets.
    5. Iterate through the opening brackets list:
       a. If there are still closing brackets to check and the current opening bracket
          index is less than the current closing bracket index:
          - Increment the nested brackets counter
          - Move to the next closing bracket
    6. Return True if the nested brackets counter is 2 or more, False otherwise.
    '''
    opening_brackets = []
    closing_brackets = []

    for i, char in enumerate(string):
        if char == '[':
            opening_brackets.append(i)
        elif char == ']':
            closing_brackets.append(i)

    closing_brackets.reverse()

    nested_brackets_counter = 0
    closing_bracket_index = 0

    for opening_bracket_index in opening_brackets:
        while closing_bracket_index < len(closing_brackets) and opening_bracket_index < closing_brackets[closing_bracket_index]:
            nested_brackets_counter += 1
            closing_bracket_index += 1

    return nested_brackets_counter >= 2