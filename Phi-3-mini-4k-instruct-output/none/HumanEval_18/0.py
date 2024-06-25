
    def how_many_times(string: str, substring: str) -> int:
        """ Find how many times a given substring can be found in the original string. Count overlapping cases.
        
        Args:
        string (str): The original string.
        substring (str): The substring to search for.
        
        Returns:
        int: The number of times the substring can be found in the original string, including overlapping cases.
        
        Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
        """
        count = 0
        start = 0
        while True:
            start = string.find(substring, start) + 1
            if start > 0:
                count += 1
            else:
                break
        return count