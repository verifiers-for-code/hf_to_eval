def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    
    Parameters:
    game (list): An array of scores.
    guess (list): An array of guesses.
    
    Returns:
    list: An array of the same length denoting how far off each guess was.
    """
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result