"""
The binary_tree_diameter function calculates the diameter of a binary tree. The diameter is defined as the length of the longest path between any two nodes in the tree, regardless of whether the path passes through the root or not.

Time: O(N), where N is the number of nodes in the binary tree, as each node is visited once. 
Space: O(N) in the worst case, as the recursion can go up to the height of the tree. 
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binary_tree_diameter(tree):
    """
    Calculate the diameter of the binary tree.

    :param tree: Binary tree
    :return: Diameter of the binary tree
    """

    return get_tree_info(tree).diameter


def get_tree_info(tree):
    """
    Helper function to calculate the diameter and height of the binary tree.

    :param tree: Binary tree
    :return: TreeInfo object containing diameter and height
    """

    if tree is None:
        return TreeInfo(0, 0)

    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)

    max_path_over_root = left_tree_info.height + right_tree_info.height
    max_diameter_so_far = max(left_tree_info.diameter, right_tree_info.diameter)
    current_diameter = max(max_path_over_root, max_diameter_so_far)
    current_height = 1 + max(left_tree_info.height, right_tree_info.height)

    return TreeInfo(current_diameter, current_height)


# Example usage
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)

    # Calculate the diameter
    print(binary_tree_diameter(tree))  # Output: 3
