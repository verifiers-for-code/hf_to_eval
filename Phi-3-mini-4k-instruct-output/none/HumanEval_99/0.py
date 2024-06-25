
    def closest_integer(value):
        """
        Create a function that takes a value (string) representing a number
        and returns the closest integer to it. If the number is equidistant
        from two integers, round it away from zero.

        :param value: str, a string representing a number
        :return: int, the closest integer to the given number
        """
        # Convert the string to a float
        num = float(value)

        # Round the number to the nearest integer
        rounded_num = round(num)

        # Check if the number is equidistant from two integers
        if abs(num - rounded_num) == 0.5:
            # If the number is positive, round it away from zero
            if num > 0:
                return rounded_num + 1
            # If the number is negative, round it away from zero
            else:
                return rounded_num - 1
        else:
            # Return the rounded number
            return rounded_num