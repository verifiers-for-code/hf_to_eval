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

    Action Plan:
    1. Compare the number of carrots needed (@need) with the number of remaining carrots (@remaining).
    2. If there are enough remaining carrots:
       a. Calculate the total number of eaten carrots (already eaten + needed).
       b. Calculate the number of carrots left after eating.
    3. If there are not enough remaining carrots:
       a. Calculate the total number of eaten carrots (already eaten + all remaining).
       b. Set the number of carrots left to 0.
    4. Return the result as a list with two elements:
       [total number of eaten carrots, number of carrots left]
    """
    if remaining >= need:
        total_eaten = number + need
        remaining_left = remaining - need
    else:
        total_eaten = number + remaining
        remaining_left = 0
    
    return [total_eaten, remaining_left]