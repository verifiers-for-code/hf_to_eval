def compare(scores, guesses):
    """Determine how far off each guess was from the actual scores."""
    differences = []
    
    # Step 2: Loop through the lists with indices
    for index in range(len(scores)):
        # Step 2.1: Retrieve the corresponding elements from both lists
        score = scores[index]
        guess = guesses[index]
        
        # Step 3: Calculate the absolute difference
        difference = abs(score - guess)
        
        # Step 4: Add the computed difference to the differences list
        if difference == 0:
            differences.append(0)
        else:
            differences.append(difference)
    
    # Step 6: Return the differences list
    return differences