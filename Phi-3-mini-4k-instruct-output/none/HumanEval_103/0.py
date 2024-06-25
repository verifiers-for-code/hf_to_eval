
    def rounded_avg(n, m):
        # Check if n is greater than m
        if n > m:
            return -1
        
        # Calculate the sum of integers from n to m
        total_sum = sum(range(n, m+1))
        
        # Calculate the average
        avg = total_sum / (m - n + 1)
        
        # Round the average to the nearest integer
        rounded_avg = round(avg)
        
        # Convert the rounded average to binary
        binary_avg = bin(rounded_avg)
        
        return binary_avg