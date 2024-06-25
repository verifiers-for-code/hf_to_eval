
    def even_odd_count(num):
        """Given an integer. return a tuple that has the number of even and odd digits respectively.

         Example:
            even_odd_count(-12) ==> (1, 1)
            even_odd_count(123) ==> (1, 2)
        """
        # Convert the number to a string to iterate over its digits
        num_str = str(abs(num))
        
        # Initialize counters for even and odd digits
        even_count = 0
        odd_count = 0
        
        # Iterate over the digits in the number
        for digit in num_str:
            # Check if the digit is even or odd
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
        # Return the tuple of even and odd digit counts
        return (even_count, odd_count)