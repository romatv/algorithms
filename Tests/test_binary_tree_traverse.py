import unittest
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    """
    Test case for the binary search tree methods. Tree is recreated before each test.
    """

    def setUp(self):
        self.tree = BinarySearchTree()

    def create_tree(self, lst):
        for i in lst:
            self.tree.insert(i)

    def test_inorder_traversal(self):
        test_list = [0, 1, 3, 2, -1]
        expected = ['-1(1)', '0(1)', '1(1)', '2(1)', '3(1)']
        self.create_tree(lst=test_list)
        result = self.tree.inorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_reverse_inorder_traversal(self):
        test_list = [0, 1, 3, 2, -1]
        expected = ['3(1)', '2(1)', '1(1)', '0(1)', '-1(1)']
        self.create_tree(lst=test_list)
        result = self.tree.reverse_inorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_same_values_reverse_inorder(self):
        test_list = [0, 1, 1, 5, 1, 3, 2, -1, -1]
        expected = ['5(1)', '3(1)', '2(1)', '1(3)', '0(1)', '-1(2)']
        self.create_tree(lst=test_list)
        result = self.tree.reverse_inorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_empty_list_inorder(self):
        test_list = []
        expected = []
        self.create_tree(lst=test_list)
        result = self.tree.inorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_oneelement_list_inorder(self):
        test_list = [5]
        expected = ['5(1)']
        self.create_tree(lst=test_list)
        result = self.tree.inorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_text_inorder(self):
        text = 'Use words length test test'
        words_list = text.split()
        test_list = [len(word) for word in words_list]
        expected = ['3(1)', '4(2)', '5(1)', '6(1)']
        self.create_tree(lst=test_list)
        result = self.tree.inorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_preorder(self):
        """Tree structure:
               27
            14    35
          10 19  31 42
        """
        test_list = [27, 14, 35, 10, 19, 31, 42]
        expected = ['27(1)', '14(1)', '10(1)', '19(1)', '35(1)', '31(1)', '42(1)']
        self.create_tree(lst=test_list)
        result = self.tree.preorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_postorder(self):
        """Tree structure:
               27
            14    35
          10 19  31 42
        """
        test_list = [27, 14, 35, 10, 19, 31, 42]
        expected = ['10(1)', '19(1)', '14(1)', '31(1)', '42(1)', '35(1)', '27(1)']
        self.create_tree(lst=test_list)
        result = self.tree.postorder_traversal(node=self.tree.root)
        self.assertEqual(first=expected, second=result)

    def test_search_node_success(self):
        test_list = [0, 1, 3, 2, -1]
        self.create_tree(lst=test_list)
        result = self.tree.search_node(node=self.tree.root, value=3)
        self.assertEqual(first=3, second=result.value)

    def test_search_node_fail(self):
        test_list = [0, 1, 3, 2, -1]
        self.create_tree(lst=test_list)
        result = self.tree.search_node(node=self.tree.root, value=5)
        self.assertIsNone(obj=result)


if __name__ == '__main__':
    unittest.main()
