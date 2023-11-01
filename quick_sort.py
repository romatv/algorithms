def quick_sort(lst):
    """
    Sorts list of integers with quick sort algorithm.

    :param lst: list of integers
    :return: sorted list of integers
    """

    if not isinstance(lst, list):
        raise TypeError('Only single list is accepted as a parameter.')
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    left = []
    right = []
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
