def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    
    Parameters:
    game (list): A list of actual scores.
    guess (list): A list of guessed scores.
    
    Returns:
    list: A list of differences between the guessed and actual scores.
    """
    # Step 1: Initialize an empty result list
    result = []
    
    # Step 2: Iterate through both 'game' and 'guess' lists simultaneously
    for actual, guessed in zip(game, guess):
        # Step 3a: If the guess is correct, append 0 to the result list
        if actual == guessed:
            result.append(0)
        # Step 3b: If the guess is incorrect, calculate the absolute difference
        else:
            result.append(abs(actual - guessed))
    
    # Step 4: Return the result list
    return result