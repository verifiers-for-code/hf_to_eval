
    def prod_signs(arr):
        # Return None for empty array
        if not arr:
            return None
        
        # Initialize product of signs and sum of magnitudes
        product_of_signs = 1
        sum_of_magnitudes = 0
        
        # Iterate through the array
        for num in arr:
            # Update product of signs
            if num > 0:
                product_of_signs *= 1
            elif num < 0:
                product_of_signs *= -1
            # Update sum of magnitudes
            sum_of_magnitudes += abs(num)
        
        # Return sum of magnitudes multiplied by product of signs
        return sum_of_magnitudes * product_of_signs