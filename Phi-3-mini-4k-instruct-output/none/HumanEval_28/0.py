
    from typing import List

    def concatenate(strings: List[str]) -> str:
        """ Concatenate list of strings into a single string

        Args:
        strings (List[str]): A list of strings to concatenate

        Returns:
        str: A single string that is the concatenation of all the strings in the input list

        Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
        >>> concatenate(['Hello', ' ', 'World'])
        'Hello World'
        """
        return ''.join(strings)