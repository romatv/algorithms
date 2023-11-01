import unittest
from quick_sort_partition import quick_sort_partition


class TestQuickSort(unittest.TestCase):
    """
    Test case for the quick sort function that returns sorted list of integers.
    """

    def test_success(self):
        test_list = [5, 4, -4, -5, 0]
        result = quick_sort_partition(lst=test_list, low=0, high=len(test_list)-1)
        self.assertEqual(first=result, second=[-5, -4, 0, 4, 5])

    def test_empty_list(self):
        test_list = []
        result = quick_sort_partition(lst=test_list, low=0, high=len(test_list)-1)
        self.assertEqual(first=result, second=[])

    def test_one_element_list(self):
        test_list = [1]
        result = quick_sort_partition(lst=test_list, low=0, high=len(test_list)-1)
        self.assertEqual(first=result, second=[1])

    def test_two_elements_lsit(self):
        test_list = [50, -10]
        result = quick_sort_partition(lst=test_list, low=0, high=len(test_list)-1)
        self.assertEqual(first=result, second=[-10, 50])

    def test_same_elements_list(self):
        test_list = [1, 1, 1, 1]
        result = quick_sort_partition(lst=test_list, low=0, high=len(test_list)-1)
        self.assertEqual(first=result, second=[1, 1, 1, 1])

    def test_incorrect_data_type(self):
        test_data = 'Text'
        with self.assertRaises(TypeError):
            quick_sort_partition(lst=test_data, low=0, high=len(test_data)-1)

    def test_diverse_data_list(self):
        test_list = [5, -1, 10, 'Text', 6, ['Another list']]
        with self.assertRaises(TypeError):
            quick_sort_partition(lst=test_list, low=0, high=len(test_list)-1)


if __name__ == '__main__':
    unittest.main()