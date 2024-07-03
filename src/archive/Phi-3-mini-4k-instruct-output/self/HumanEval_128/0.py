def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.
    """
    if not arr:
        return None

    product_of_signs = 1
    positive_numbers = []
    negative_numbers = []

    for num in arr:
        if num == 0:
            continue
        sign = 1 if num > 0 else -1
        product_of_signs *= sign

        if num > 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)

    product_of_positives = 1
    product_of_negatives = 1

    for num in positive_numbers:
        product_of_positives *= abs(num)

    for num in negative_numbers:
        product_of_negatives *= abs(num)

    return product_of_signs * (product_of_positives + product_of_negatives)