
    def monotonic(l: list):
        """Return True if list elements are monotonically increasing or decreasing.
        
        Args:
        l (list): A list of integers.
        
        Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
        
        Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
        """
        # Check if the list is empty or has only one element
        if len(l) < 2:
            return True
        
        # Check if the list is monotonically increasing
        increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
        
        # Check if the list is monotonically decreasing
        decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
        
        return increasing or decreasing