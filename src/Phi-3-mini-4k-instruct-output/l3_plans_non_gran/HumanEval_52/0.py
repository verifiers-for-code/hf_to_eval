def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    

    Action Plan:
    1. Define the function below_threshold with two parameters: l (a list of numbers) and t (an integer threshold)
    2. Initialize a loop to iterate through each number in the list l
    3. Inside the loop, compare each number with the threshold t
    4. If any number is not below the threshold (i.e., greater than or equal to t), immediately return False
    5. If the loop completes without finding any number greater than or equal to t, return True
    6. Consider using a built-in function or a concise syntax to simplify the comparison and iteration process"""
    for num in l:
        if num >= t:
            return False
    return True