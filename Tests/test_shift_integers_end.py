import unittest
from shift_integers_end import shift_integers_end


class TestShiftIntegersEnd(unittest.TestCase):
    """
    Test case for the function that has to shift selected integers in the list to the end of given list copy,
    and return this copy of list as a result.
    """

    def test_zeros_to_end(self):
        test_list = [0, 1, 0, 2, -1, -2, 3]
        result = shift_integers_end(lst=test_list, element=0)
        self.assertEqual(first=result, second=[1, 2, -1, -2, 3, 0, 0])

    def test_negative_to_end(self):
        test_list = [0, 1, 0, 2, -1, -2, 3]
        result = shift_integers_end(lst=test_list, element=-1)
        self.assertEqual(first=result, second=[0, 1, 0, 2, -2, 3, -1])

    def test_no_element_to_shift(self):
        test_list = [1, 2, -1, -2, 3]
        result = shift_integers_end(lst=test_list, element=0)
        self.assertEqual(first=result, second=[1, 2, -1, -2, 3])

    def test_empty_list(self):
        test_list = []
        result = shift_integers_end(lst=test_list, element=0)
        self.assertEqual(first=result, second=[])

    def test_incorrect_data_type(self):
        test_data = {'a': 1}
        with self.assertRaises(TypeError):
            shift_integers_end(lst=test_data, element=0)

    def test_diverse_data_list(self):
        test_list = [0, 1, 'Text', 0, 2, -1, -2, 3, ['Another list']]
        result = shift_integers_end(lst=test_list, element=0)
        self.assertEqual(first=result, second=[1, 'Text', 2, -1, -2, 3, ['Another list'], 0, 0])


if __name__ == '__main__':
    unittest.main()
