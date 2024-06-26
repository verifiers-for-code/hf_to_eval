def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    
    Parameters:
    game (list): A list of actual scores.
    guess (list): A list of guessed scores.
    
    Returns:
    list: A list of differences between the guessed and actual scores.
    """
    # Initialize an empty result list to store the differences.
    result = []
    
    # Iterate through both 'game' and 'guess' lists simultaneously using zip().
    for actual, guessed in zip(game, guess):
        # If the guess is correct (actual == guessed), append 0 to the result list.
        if actual == guessed:
            result.append(0)
        # If the guess is incorrect, calculate the absolute difference between actual and guessed scores,
        # and append this value to the result list.
        else:
            result.append(abs(actual - guessed))
    
    # After processing all pairs, return the result list.
    return result