def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

    Args:
    number (int): the number of carrots that you have eaten.
    need (int): the number of carrots that you need to eat.
    remaining (int): the number of remaining carrots thet exist in stock

    Returns:
    List[int]: a list containing the total number of eaten carrots after your meals and the number of carrots left after your meals.

    Constraints:
    0 <= number <= 1000
    0 <= need <= 1000
    0 <= remaining <= 1000
    """
    total_eaten = number + need
    if remaining >= need:
        remaining -= need
        return [total_eaten, remaining]
    else:
        total_eaten -= remaining
        return [total_eaten, 0]