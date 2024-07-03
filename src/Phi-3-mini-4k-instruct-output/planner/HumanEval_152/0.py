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
    1. Understand the input: two arrays of equal length, where each index represents a match between a score and a guess.
    2. Initialize an empty array (results) to store the differences between the guesses and scores.
    3. Iterate through the input arrays using a loop:
        a. For each iteration, access the current score and guess at the same index.
        b. Calculate the absolute difference between the score and guess using the abs() function.
        c. Store the result in the results array at the current index.
    4. After the loop, return the results array, which now contains the differences between the guesses and scores.
    5. Ensure the function returns an array of the same length as the input arrays.
    
    Note: Use a loop to iterate through the input arrays, and the abs() function to calculate the absolute difference.
    Be careful to store the results in the correct array and index."""
    
    results = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        results.append(diff)
    return results