def insertion_sort(lst):
    """
    Sorts the list of integers by insertion sorts algorithm.

    :param lst: list of integers
    :return: sorted list
    """

    for i in range(1, len(lst)):
        current_element = lst[i]
        j = i - 1
        while j >= 0 and current_element < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_element
    return lst
