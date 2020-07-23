import unittest
from .binary_tree import TreeNode


def helper(root: TreeNode) -> bool:
    return divide_conquer(root)[0]


# 这题很适合用分治法，返回值是(是否平衡,深度)
# 而当前节点是否平衡与 左子树高度 和 右子树高度信息有关，所以用分治法效率比前序遍历要高
def divide_conquer(root: TreeNode) -> (bool, int):
    if root is None:
        # 空树也是平衡二叉树
        return True, 0
    left_subtree_is_balanced, left_subtree_height = divide_conquer(root.left)
    right_subtree_is_balanced, right_subtree_height = divide_conquer(root.right)
    root_height = max(left_subtree_height, right_subtree_height) + 1
    if not left_subtree_is_balanced or not right_subtree_is_balanced:
        return False, root_height
    if abs(left_subtree_height - right_subtree_height) > 1:
        return False, root_height
    return True, root_height


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], True),
        ([1, None, 2, None, None, 3, 4], False),
    ]

    def test_list_all_root_to_leaf_paths(self):
        for binary_tree, is_balanced in self.TEST_CASES:
            # root = TreeNode.from_list(binary_tree)
            root = TreeNode(1)
            root.right = TreeNode(2)
            root.right.left = TreeNode(3)
            root.right.right = TreeNode(4)
            print(root)
            # self.assertEqual(is_balanced, helper(root))
