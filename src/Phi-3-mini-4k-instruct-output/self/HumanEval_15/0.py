def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Action Plan:
    1. Initialize an empty string variable to hold the sequence
    2. Use a loop to iterate through each number from 0 to n (inclusive)
        - Include an iterable range with `range(n + 1)`
    
    3. In each iteration, convert the current number to a string and concatenate it with the existing sequence
        - Use the `.join()` method for string concatenation with spaces as the separator
    
    4. Return the final string after the loop completes
    
    5. Consider the edge case of n=0 to ensure the function still returns the correct single-digit string "0"
    """
    sequence = ""
    for i in range(n + 1):
        sequence += str(i) + " "
    return sequence.strip()