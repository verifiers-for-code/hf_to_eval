def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    

    Action Plan:
    1. Begin with understanding the problem requirements and constraints:
        a. Input variables: number of eaten carrots, number of carrots needed, and number of remaining carrots
        b. Identify the key outcome: total eaten carrots and remaining carrots after eating
    
    2. Implement the function's logic:
        a. Initialize a variable to store the sum of eaten carrots (eaten_total)
        b. Check if the number of remaining carrots is less than the number needed
            i. If so, return [eaten_total + remaining, 0] as the rabbit has eaten all available carrots
            ii. Otherwise, update the eaten_total by adding the sum of remaining carrots and the needed need
        c. Calculate the remaining carrots after eating (eaten_remaining) as the difference between the needed and eaten_total
    
    3. Edge cases:
        a. When remaining carrots are zero or negative
        b. When the need is negative
    
    4. Return the final result in an array format [eaten_total, eaten_remaining]"""
    
    # Step 1: Initialize the sum of eaten carrots
    eaten_total = number
    
    # Step 2: Check if there are enough remaining carrots
    if remaining < need:
        # If not, return the total eaten carrots plus the remaining carrots, and 0 for remaining
        return [eaten_total + remaining, 0]
    else:
        # If there are enough remaining carrots, update the eaten_total
        eaten_total += need
        
        # Step 3: Calculate the remaining carrots after eating
        eaten_remaining = need - (remaining - need)
        
        # Step 4: Return the final result
        return [eaten_total, eaten_remaining]