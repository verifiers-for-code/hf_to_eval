def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    
    Parameters:
    game (list): An array of scores.
    guess (list): An array of guesses.
    
    Returns:
    list: An array of the same length as the input arrays, denoting how far off each guess was.
    """
    # Initialize an empty array to store the differences between the guesses and scores
    results = []
    
    # Iterate through the input arrays using a loop
    for i in range(len(game)):
        # Access the current score and guess at the same index
        score = game[i]
        guess_value = guess[i]
        
        # Calculate the absolute difference between the score and guess
        difference = abs(score - guess_value)
        
        # Store the result in the results array at the current index
        results.append(difference)
    
    # Return the results array
    return results