
    from typing import List

    def unique(l: List[int]) -> List[int]:
        """Return sorted unique elements in a list

        Args:
        l (List[int]): A list of integers

        Returns:
        List[int]: A sorted list of unique integers

        Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
        """
        return sorted(set(l))