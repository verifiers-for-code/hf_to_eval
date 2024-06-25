
    from typing import List, Tuple

    def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
        """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
        """
        # Sort the list of numbers
        numbers.sort()
        
        # Initialize the minimum difference and the closest pair
        min_diff = float('inf')
        closest_pair = (0, 0)
        
        # Iterate through the list, comparing each pair of adjacent numbers
        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            
            # Update the minimum difference and closest pair if a smaller difference is found
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[i + 1])
                
        return closest_pair