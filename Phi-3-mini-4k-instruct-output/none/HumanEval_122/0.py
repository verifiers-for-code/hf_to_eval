
    def add_elements(arr, k):
        """
        Given a non-empty array of integers arr and an integer k, return
        the sum of the elements with at most two digits from the first k elements of arr.

        :param arr: List[int]
        :param k: int
        :return: int
        """
        # Filter elements with at most two digits and sum them
        return sum(x for x in arr[:k] if 10 <= x <= 99)