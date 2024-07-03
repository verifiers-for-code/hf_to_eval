def compare(game, guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    

    Action Plan:
    1. Initialize an empty list called `differences` to store the result values.
    
    2. Loop through the lists with indices:
        - For each index, retrieve the corresponding elements from both lists (e.g., `scores[index]`, `guesses[index]`).
    
    3. Calculate the absolute difference between the elements from both lists:
        - Compute `difference = abs(scores[index] - guesses[index])`.
    
    4. Add the computed difference to the `differences` list:
        - If the difference is 0, append 0 to the list, representing a correct guess.
        - Otherwise, append the actual difference value.
    
    5. Continue iterating through the lists until all indices are processed.
    
    6. Once the loop ends, return the `differences` list as the final result.
    
    7. Note any edge cases:
        - If the lists have different lengths, handle it as an error or an unexpected scenario.
        - Consider how to deal with empty lists or lists with only elements that need to be compared (e.g., all elements may be zero)."""

    # Check if the input lists have the same length
    if len(game) != len(guess):
        raise ValueError("The input lists must have the same length.")

    differences = []
    for index in range(len(game)):
        score = game[index]
        guess_value = guess[index]
        difference = abs(score - guess_value)
        differences.append(difference)

    return differences