def compare(game, guess):
    """
    I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    Example:
    
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    
    Action Plan:
    1. Define the function compare with two parameters: game and guess
    2. Initialize an empty list to store the results (e.g., compare_result)
    3. Iterate through the game and guess arrays simultaneously using a loop (e.g., for loop)
    4. Within the loop:
        a. Calculate the absolute difference between the current score (game[i]) and the current guess (guess[i])
        b. Append the calculated difference to the compare_result list
    5. After the loop, return the compare_result list
    6. Ensure the function handles edge cases, such as empty input arrays or arrays of different lengths
    """
    compare_result = []
    if len(game) != len(guess):
        return "Error: The game and guess arrays must have the same length."
    for i in range(len(game)):
        if game[i] == guess[i]:
            compare_result.append(0)
        else:
            compare_result.append(abs(game[i] - guess[i]))
    return compare_result