import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """
    Test case for the bubble sort function that returns sorted list of integers.
    """

    def test_success(self):
        test_list = [5, 4, -4, -5, 0]
        result = bubble_sort(lst=test_list)
        self.assertEqual(first=result, second=[-5, -4, 0, 4, 5])

    def test_empty_list(self):
        test_list = []
        result = bubble_sort(lst=test_list)
        self.assertEqual(first=result, second=[])

    def test_one_element_list(self):
        test_list = [1]
        result = bubble_sort(lst=test_list)
        self.assertEqual(first=result, second=[1])

    def test_two_elements_lsit(self):
        test_list = [50, -10]
        result = bubble_sort(lst=test_list)
        self.assertEqual(first=result, second=[-10, 50])

    def test_same_elements_list(self):
        test_list = [1, 1, 1, 1]
        result = bubble_sort(lst=test_list)
        self.assertEqual(first=result, second=[1, 1, 1, 1])

    def test_incorrect_data_type(self):
        test_data = 'Text'
        with self.assertRaises(TypeError):
            bubble_sort(lst=test_data)

    def test_diverse_data_list(self):
        test_list = [5, -1, 10, 'Text', 6, ['Another list']]
        with self.assertRaises(TypeError):
            bubble_sort(lst=test_list)


if __name__ == '__main__':
    unittest.main()
