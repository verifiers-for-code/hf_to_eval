
    def by_length(arr):
        # Define a dictionary to map numbers to their names
        num_to_name = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        
        # Filter out numbers that are not between 1 and 9
        filtered_arr = [num for num in arr if 1 <= num <= 9]
        
        # Sort the filtered array
        sorted_arr = sorted(filtered_arr)
        
        # Reverse the sorted array
        reversed_arr = sorted_arr[::-1]
        
        # Replace each number with its corresponding name
        result = [num_to_name[num] for num in reversed_arr]
        
        return result