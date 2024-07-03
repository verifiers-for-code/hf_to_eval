def compare(game, guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    Action Plan:
    1. Initialize an empty result list to store the differences.
    2. Iterate through both 'game' and 'guess' lists simultaneously using zip() or range(len(game)).
    3. For each pair of elements (actual score and guessed score):
       a. If the guess is correct (actual == guessed), append 0 to the result list.
       b. If the guess is incorrect, calculate the absolute difference between actual and guessed scores,
          and append this value to the result list.
    4. After processing all pairs, return the result list.

    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    result = []
    for actual, guessed in zip(game, guess):
        if actual == guessed:
            result.append(0)
        else:
            result.append(abs(actual - guessed))
    return result