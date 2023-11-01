def bubble_sort(lst):
    """
    Sorts list of integers with bubble sort algorithm.
    :param lst: list of integers
    :return: sorted list of integers
    """

    if not isinstance(lst, list):
        raise TypeError('Only single list is accepted as a parameter.')
    if len(lst) <= 1:
        return lst

    n = len(lst)
    for i in range(n):
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        n -= 1

    return lst
