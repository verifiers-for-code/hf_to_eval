
    from typing import List
    
    def common(l1: List[int], l2: List[int]) -> List[int]:
        """Return sorted unique common elements for two lists.
        
        Args:
        l1 (List[int]): First list of integers
        l2 (List[int]): Second list of integers
        
        Returns:
        List[int]: Sorted unique common elements for the two lists
        
        Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
        """
        # Convert lists to sets to remove duplicates and find the intersection
        common_elements = set(l1).intersection(set(l2))
        
        # Convert the set back to a list and sort it
        sorted_common_elements = sorted(list(common_elements))
        
        return sorted_common_elements