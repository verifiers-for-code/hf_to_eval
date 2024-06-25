
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        """Return the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))

    def largest_prime_sum_of_digits(lst):
        """Find the largest prime value in the list and return the sum of its digits."""
        largest_prime = None
        for num in lst:
            if is_prime(num):
                if largest_prime is None or num > largest_prime:
                    largest_prime = num
        return sum_of_digits(largest_prime)