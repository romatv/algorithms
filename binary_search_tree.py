class Node:
    """
    Class defining a node for a binary search tree (BST).

    Each node in the BST contains a value and an optional 'count' parameter, which is updated if the same value
    is encountered during tree construction.

    Parameters:
    value: The value of the node.

    Attributes:
    left (Node): The left child node.
    right (Node): The right child node.
    value: The value stored in the node.
    count (int): The count of how many times the value appears in the tree.
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.count = 1


class BinarySearchTree:
    """
    Class defining methods for constructing and traversing a binary search tree (BST).
    A binary search tree is a data structure that allows efficient insertion, deletion, and retrieval of values
    while maintaining the property that for each node:
    - All values in the left subtree are less than or equal to the node's value.
    - All values in the right subtree are greater than the node's value.

    Attributes:
    root (Node): The root node of the binary search tree.
    result: list, placeholder for result of traversal.

    Methods:
    - insert(value): Insert a value into the binary search tree.
    - inorder_traversal(node): Perform an inorder traversal of the BST, returning values in ascending order.
    - reverse_inorder_traversal(node): Perform a reverse_inorder traversal of the BST, returning values with counts.

    Note: This implementation supports duplicate values.
    """
    def __init__(self):
        self.root = None
        self.result = []

    def insert(self, value):
        """
        Insert a value into the binary search tree.
        If the value already exists in the tree, its count will be incremented.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(node=self.root, value=value)

    def insert_recursive(self, node, value):
        """
        Recursively insert a value into the binary search tree.
        """
        if value == node.value:
            node.count += 1
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node=node.left, value=value)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node=node.right, value=value)

    def inorder_traversal(self, node):
        """
        Perform an inorder traversal of the binary search tree.
        """
        if node is not None:
            self.inorder_traversal(node.left)
            self.result.append(f'{node.value}({node.count})')
            self.inorder_traversal(node.right)
        return self.result

    def reverse_inorder_traversal(self, node):
        """
        Perform a reverse_inorder traversal of the binary search tree.
        """
        if node is not None:
            self.reverse_inorder_traversal(node.right)
            self.result.append(f'{node.value}({node.count})')
            self.reverse_inorder_traversal(node.left)
        return self.result

    def preorder_traversal(self, node):
        """
        Perform a preorder traversal of the binary search tree.
        """
        if node is not None:
            self.result.append(f'{node.value}({node.count})')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        return self.result

    def postorder_traversal(self, node):
        """
        Perform a postorder traversal of the binary search tree.
        """
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            self.result.append(f'{node.value}({node.count})')
        return self.result

    def search_node(self, node, value):
        """
        Search for a node with chosen value in binary search tree.
        Returns node with value if found, otherwise returns None.
        """
        if node is None or value == node.value:
            return node
        if value < node.value:
            return self.search_node(node.left, value)
        if value > node.value:
            return self.search_node(node.right, value)

    def delete_node(self, node, value):
        if node is None or value == node.value:
            return node
        if value < node.value:
            return self.search_node(node.left, value)
        if value > node.value:
            return self.search_node(node.right, value)
