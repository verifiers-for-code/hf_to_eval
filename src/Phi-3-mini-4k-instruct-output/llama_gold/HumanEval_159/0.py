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
    1. Understand the inputs: number (already eaten carrots), need (carrots to eat), and remaining (available carrots).
    2. Check if the remaining carrots are sufficient to meet the need:
       a. If there are enough remaining carrots (need <= remaining):
          - Calculate the total number of eaten carrots by adding the need to the number.
          - Calculate the remaining carrots by subtracting the need from the remaining carrots.
       b. If there are not enough remaining carrots (need > remaining):
          - Calculate the total number of eaten carrots by adding the remaining carrots to the number.
          - Set the remaining carrots to 0, as the rabbit will eat all remaining carrots.
    3. Return a list containing the total number of eaten carrots and the remaining carrots.
    """
    if need <= remaining:
        total_eaten = number + need
        remaining_carrots = remaining - need
    else:
        total_eaten = number + remaining
        remaining_carrots = 0

    return [total_eaten, remaining_carrots]