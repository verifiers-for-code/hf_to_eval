
    from typing import List

    def median(l: List[int]) -> float:
        """Return median of elements in the list l.

        Args:
        l (List[int]): A list of integers.

        Returns:
        float: The median of the elements in the list.

        Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        10.0
        """
        l.sort()
        n = len(l)
        if n % 2 == 0:
            return (l[n//2 - 1] + l[n//2]) / 2
        else:
            return l[n//2]