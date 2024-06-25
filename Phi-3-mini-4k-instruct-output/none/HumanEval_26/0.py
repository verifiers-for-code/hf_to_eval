
    from typing import List
    from collections import OrderedDict

    def remove_duplicates(numbers: List[int]) -> List[int]:
        """ From a list of integers, remove all elements that occur more than once.
        Keep order of elements left the same as in the input.
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
        """
        # Use OrderedDict to keep the order of elements
        unique_numbers = OrderedDict.fromkeys(numbers)
        
        # Convert the OrderedDict back to a list
        return list(unique_numbers.keys())