
    def get_row(lst, x):
        """
        Finds coordinates of integer x in a 2D list, sorted by rows and columns.
        """
        result = []
        for i, row in enumerate(lst):
            for j, val in enumerate(row):
                if val == x:
                    result.append((i, j))
        result.sort(key=lambda x: (x[0], -x[1]))
        return result