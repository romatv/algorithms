"""
About the partition function and what it does:

Consider the list arr as [4, 1, 3, 9, 6, 7], low as 0, and high as 5.
The pivot is selected as the last element, which is 7.
Initialize i to low - 1, which is -1.
The loop begins, and j iterates from low (0) to high - 1 (4).

For j = 0, arr[j] is 4, which is less than the pivot 7. So, i is incremented to 0, and arr[0] and arr[0] are swapped
(no change).

For j = 1, arr[j] is 1, which is less than the pivot. i becomes 1, and arr[1] and arr[1] are swapped (no change).

For j = 2, arr[j] is 3, which is less than the pivot. i becomes 2, and arr[2] and arr[2] are swapped (no change).

For j = 3, arr[j] is 9, which is greater than the pivot. i remains 2, and no swapping occurs.

For j = 4, arr[j] is 6, which is less than the pivot. i becomes 3, and arr[3] and arr[4] (swaps elements 9 and 6) are
swapped. The list is now [4, 1, 3, 6, 9, 7].

The loop ends, and the pivot (7) is swapped with arr[3]. The list is now [4, 1, 3, 6, 7, 9]. The pivot is now in its
correct sorted position.

The function returns i + 1, which is 4.

The partition function correctly rearranges the list so that elements less than or equal to the pivot are on the
left, the pivot is in its correct position, and elements greater than the pivot are on the right. This is a
fundamental step in the Quick Sort algorithm."""


def partition(lst, low, high):
    """
    Places chosen element at index --high-- in such place that all elements smaller are on the left of it, and
    bigger on the right. then returns index of this element in a resulted list.

    :param lst: list of integers
    :param low: starting index of sorting (should be 0 on first call)
    :param high: index of last element in the list
    :return: index of pivot element
    """
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort_partition(lst, low, high):
    """
    Sorts list in place by using partition function to choose the pivot element and place it in the correct
    position so all elements smaller will be on the left and bigger on the right.

    :param lst: list of integers
    :param low: starting index of sorting (should be 0 on first call)
    :param high: index of last element in the list
    :return: sorted list
    """

    if not isinstance(lst, list):
        raise TypeError('Only single list is accepted as a parameter.')
    if len(lst) <= 1:
        return lst

    if low < high:
        pi = partition(lst, low, high)  # Partition the list and get the pivot's index
        quick_sort_partition(lst, low, pi - 1)  # Recursively sort the left sublist
        quick_sort_partition(lst, pi + 1, high)  # Recursively sort the right sublist

    return lst
