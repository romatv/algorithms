from collections import deque


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
    count (int): The count of how many times the value appears in the tree. Default is 1.
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
    node (Node): The node of the binary search tree.
    result: list, placeholder for results of traversal or other methods. Added for test convenience,
    though shall not be used if tree is used in real cases, as it's not self cleared after traversals.
    In case of real use, add separate result list in each method or use other way.

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

    def find_max_node(self, node):
        """
        Find node with maximum value and return it.
        """
        if node.right is not None:
            return self.find_max_node(node.right)
        else:
            return node

    def find_min_node(self, node):
        """
        Find node with minimum value and return it.
        """
        if node.left is not None:
            return self.find_min_node(node.left)
        else:
            return node

    def search_node(self, node, value):
        """
        Search for a node with chosen value.
        Returns node with value if found, otherwise returns None.
        """
        if node is None or value == node.value:
            return node
        if value < node.value:
            return self.search_node(node.left, value)
        if value > node.value:
            return self.search_node(node.right, value)

    def delete_node(self, node, value):
        """
        Deletes node with specified value and returns the modified node (tree) rearranged after
        deletion of required node.
        It handles deletion of leaf node, node with one child and node with both children.
        """

        # If current node is None, it's an empty tree.
        if node is None:
            return node

        # If value to delete is bigger than current node value, earch in the right subtree, else in left.
        if node.value < value:
            node.right = self.delete_node(node.right, value)
        elif node.value > value:
            node.left = self.delete_node(node.left, value)

        # If the value matches the current node value, it needs to be deleted.
        # So we check if this node has one child: left or right.
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # If it has both left and right children, means that we have to find the smallest successor of
            # current node in right subtree, and replace current node value with this successor value.
            current = node.right
            # Here we go to the deepest left node.
            while current.left is not None:
                current = current.left
            # Here we assign successor value to current node value.
            node.val = current.value
            # Here we delete the in-order successor from that right subtree.
            node.right = self.delete_node(node.right, node.value)
        # return modified node after the deletion.
        return node

    def bfs_level_order_traversal(self, root):
        """
        Performs level order tree search, starting from root down to leafes.
        Returns list of node values and their counts as result.
        """
        if root is None:
            return

        # Create a double edge queue data structure to effectively
        # pop elements with O(1) time complexity. Then append root node to it.
        queue = deque()
        queue.append(root)

        # While queue is not empty, pop its node and write value to result list.
        # Then add left and right childs of this node to queue and repeat.
        while queue:
            node = queue.popleft()
            self.result.append(f'{node.value}({node.count})')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return self.result

    def bfs_level_order_traversal_with_height(self, root):
        """
        Performs level order tree search, starting from root down to leafes, by keeping track of tree height.
        Returns list of node values and their counts as result.
        This adds posibility to perform specific operations at chosen level height (depth) if needed.
        """
        if root is None:
            return

        queue = deque()
        queue.append(root)

        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            # Result of current level
            level_result = []

            for _ in range(level_size):
                node = queue.popleft()
                level_result.append(f'{node.value}({node.count})')

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            for i in level_result:
                self.result.append(i)

        return self.result
