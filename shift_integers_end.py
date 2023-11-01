"""
 This function will shift all required elements (0 in example) to the end of list without sorting or
 changing the order of other integers. List is modified in place.
 We use pointer to keep track of position of zero and swap next element with it if this element is not another zero.
 Here is example of sequence [1,5,0,3]:
 1. Element with index 0 is 1. It's not equal to 0. Current zero position is stated as index 0.
 2. So element is swapped with itself and no problem occures. Zero position index increased to 1.
 3. Element with index 1 is 5. It's not equal to 5. Element is swapped with itself. Zero position is 2.
 4. Element with index 2 is 0. Nothing happens.
 5. Element with index 3 is 3. It's not equal to 0. Element is swapped with element at zero position which is at index 2.
 6. No more elements.

 Test is located in test folder
 """


def shift_integers_end(lst, element):
    """
    Shift all selected elements to the end of list.

    :param lst: list of integers
    :param element: integer to search
    :return: list
    """
    if not isinstance(lst, list):
        raise TypeError('Incorrect data type, function takes only single list as a parameter.')

    if len(lst) <= 1:
        return lst

    element_position = 0

    for i in range(len(lst)):
        if lst[i] != element:
            lst[i], lst[element_position] = lst[element_position], lst[i]
            element_position += 1

    return lst
