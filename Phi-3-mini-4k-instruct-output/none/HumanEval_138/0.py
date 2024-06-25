
    def is_equal_to_sum_even(n):
        """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
        Example
        is_equal_to_sum_even(4) == False
        is_equal_to_sum_even(6) == False
        is_equal_to_sum_even(8) == True
        """
        # Iterate through all possible combinations of 4 even numbers
        for a in range(0, n//2 + 1, 2):
            for b in range(a, n//2 + 1, 2):
                for c in range(b, n//2 + 1, 2):
                    for d in range(c, n//2 + 1, 2):
                        # Check if the sum of the 4 even numbers equals n
                        if a + b + c + d == n:
                            return True
        return False