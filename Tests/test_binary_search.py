import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    """
    Test case for the binary search function that returns True if element is found and False otherwise.
    """

    def test_success(self):
        test_list = [-2, -1, 0, 1, 2]
        result = binary_search(lst=test_list, target=0)
        self.assertTrue(expr=result)

    def test_fail(self):
        test_list = [-2, -1, 0, 1, 2]
        result = binary_search(lst=test_list, target=5)
        self.assertFalse(expr=result)

    def test_empty_list(self):
        test_list = []
        result = binary_search(lst=test_list, target=0)
        self.assertEqual(first=result, second=[])

    def test_one_element_list(self):
        test_list = [0]
        result = binary_search(lst=test_list, target=0)
        self.assertTrue(expr=result)

    def test_two_equal_elements_list(self):
        test_list = [-2, -1, 0, 1, 2, 0]
        result = binary_search(lst=test_list, target=0)
        self.assertTrue(expr=result)

    def test_incorrect_data_type(self):
        test_data = 'Incorrect data type'
        with self.assertRaises(expected_exception=TypeError):
            binary_search(lst=test_data, target=0)

    def test_diverse_data_list(self):
        test_list = [-2, -1, 'Text', 1, 2, 0, ['Another list']]
        with self.assertRaises(expected_exception=TypeError):
            binary_search(lst=test_list, target=0)


if __name__ == '__main__':
    unittest.main()
