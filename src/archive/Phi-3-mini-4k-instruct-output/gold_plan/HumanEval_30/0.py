def get_positive(l: list):
    """Return only positive numbers in the list.

    Action Plan:
    1. Understand the function's purpose: filter out non-positive numbers from the input list.
    2. Input: 'l' is a list of numbers (can be integers or floats).
    3. Create a new list containing only the positive numbers from the input list.
    4. Use a concise Python construct to iterate through the input list and apply a condition.
    5. For each element in the input list, check if it's greater than 0.
    6. If an element satisfies the condition, include it in the new list.
    7. Return the new list containing only positive numbers.
    """
    return [num for num in l if num > 0]