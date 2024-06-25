
    def count_nums(arr):
        """
        Write a function count_nums which takes an array of integers and returns
        the number of elements which has a sum of digits > 0.
        If a number is negative, then its first signed digit will be negative:
        e.g. -123 has signed digits -1, 2, and 3.
        """
        def sum_of_digits(n):
            """
            Helper function to calculate the sum of digits of a number.
            """
            if n == 0:
                return 0
            sign = -1 if n < 0 else 1
            n = abs(n)
            sum = 0
            while n > 0:
                sum += n % 10
                n //= 10
            return sign * sum

        count = 0
        for num in arr:
            if sum_of_digits(num) > 0:
                count += 1
        return count