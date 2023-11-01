def binary_search(lst, target):
    """
    Performs binary search on a given list.
     
    :param lst: list of integers
    :param target: integer to search
    :return: bool
    """

    if not isinstance(lst, list):
        raise TypeError('Incorrect data type, function takes only single list as a parameter.')

    if len(lst) <= 1:
        return lst

    lst = sorted(lst)
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            left = mid + 1
        else:
            right -= mid - 1
    return False
