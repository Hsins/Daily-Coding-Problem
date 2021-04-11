class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def count_unival_subtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.is_unival(root)

        return self.count

    def is_unival(self, root: TreeNode) -> bool:
        # Leaf Node must be an Univalue Tree, return True
        if root is None:
            return True

        # Traverse tree with DFS
        left = self.is_unival(root.left)
        right = self.is_unival(root.right)

        # If both children are Univalue Tree and root.value is
        # equal to both children's values. Then the tree of root
        # node is an Univalue Tree
        if left and right:
            if (root.left is not None) and (root.val != root.left.val):
                return False
            if (root.right is not None) and (root.val != root.right.val):
                return False
            self.count += 1
            return True
        return False
