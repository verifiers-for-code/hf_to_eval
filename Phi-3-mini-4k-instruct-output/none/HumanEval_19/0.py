
    from typing import List

    def sort_numbers(numbers: str) -> str:
        """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
        Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
        Return the string with numbers sorted from smallest to largest
        >>> sort_numbers('three one five')
        'one three five'
        """
        # Convert the input string into a list of words
        words = numbers.split()
        
        # Create a dictionary to map words to their corresponding integer values
        word_to_num = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }
        
        # Convert the words into integers using the dictionary
        nums = [word_to_num[word] for word in words]
        
        # Sort the list of integers
        nums.sort()
        
        # Convert the sorted integers back into words
        sorted_words = [list(word_to_num.keys())[list(word_to_num.values()).index(num)] for num in nums]
        
        # Join the sorted words into a string
        sorted_numbers = ' '.join(sorted_words)
        
        return sorted_numbers