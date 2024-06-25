
    def correct_bracketing(brackets: str):
        """ brackets is a string of "<" and ">".
        return True if every opening bracket has a corresponding closing bracket.

        >>> correct_bracketing("<")
        False
        >>> correct_bracketing("<>")
        True
        >>> correct_bracketing("<<><>>")
        True
        >>> correct_bracketing("><<>")
        False
        """

        # Initialize a counter to keep track of the balance of brackets
        balance = 0

        # Iterate through each character in the input string
        for char in brackets:
            # If the character is an opening bracket, increment the balance
            if char == "<":
                balance += 1
            # If the character is a closing bracket, decrement the balance
            elif char == ">":
                balance -= 1

            # If the balance becomes negative at any point, return False
            if balance < 0:
                return False

        # If the balance is zero at the end, return True
        return balance == 0