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
    1. Ensure the input arrays 'game' and 'guess' have the same length.
    2. Initialize an empty list to store the result.
    3. Iterate through the input arrays in parallel (using their indices or zip functionality):
       a. For each pair of corresponding elements, calculate the absolute difference.
       b. If the difference is 0, it's a correct guess, so add 0 to the result list.
       c. If the difference is not 0, it's an incorrect guess, so add the absolute difference to the result list.
    4. Return the result list containing the differences between the game scores and guesses."""
    
    # Step 1: Ensure the input arrays 'game' and 'guess' have the same length.
    if len(game) != len(guess):
        raise ValueError("The input arrays 'game' and 'guess' must have the same length.")
    
    # Step 2: Initialize an empty list to store the result.
    result = []
    
    # Step 3: Iterate through the input arrays in parallel (using their indices or zip functionality).
    for g, gu in zip(game, guess):
        # a. For each pair of corresponding elements, calculate the absolute difference.
        difference = abs(g - gu)
        
        # b. If the difference is 0, it's a correct guess, so add 0 to the result list.
        if difference == 0:
            result.append(0)
        # c. If the difference is not 0, it's an incorrect guess, so add the absolute difference to the result list.
        else:
            result.append(difference)
    
    # Step 4: Return the result list containing the differences between the game scores and guesses.
    return result