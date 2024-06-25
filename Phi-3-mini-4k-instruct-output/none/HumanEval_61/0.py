
    def correct_bracketing(brackets: str):
        """ brackets is a string of "(" and ")".
        return True if every opening bracket has a corresponding closing bracket.

        >>> correct_bracketing("(")
        False
        >>> correct_bracketing("()")
        True
        >>> correct_bracketing("(()())")
        True
        >>> correct_bracketing(")(()")
        False
        """
        stack = []
        for bracket in brackets:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
        return len(stack) == 0