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
    

    1. Initialize an empty list to store the results
       - This list will hold the differences between each guess and score
    
    2. Iterate through each index of the input arrays:
       a. Calculate the absolute difference between the score and guess at the current index
       b. Append the calculated difference to the results list
    
    3. Handle correct guesses:
       - If the score and guess are equal, append 0 to the results list
    
    4. Handle incorrect guesses:
       - If the score and guess are not equal, append the calculated difference to the results list
    
    5. Return the results list
       - This list will contain the differences between each guess and score
    
    Additional implementation details:
    - Use a loop to iterate through the input arrays
    - Use the absolute difference function (abs()) to calculate the difference between the score and guess
    - Use a conditional statement (if-else) to handle correct and incorrect guesses
    - Ensure the function handles empty input arrays correctly
    - Consider using a list comprehension or a generator expression to create the results list"""
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate through each index of the input arrays
    for i in range(len(game)):
        # Calculate the absolute difference between the score and guess at the current index
        diff = abs(game[i] - guess[i])
        
        # Append the calculated difference to the results list
        results.append(diff)
    
    # Return the results list
    return results