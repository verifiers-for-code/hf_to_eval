
    def sort_array(arr):
        # Helper function to count the number of ones in binary representation
        def count_ones(num):
            return bin(num).count('1')

        # Sort the array using a custom key
        arr.sort(key=lambda x: (count_ones(x), x))
        return arr