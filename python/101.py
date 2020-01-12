# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def symmetric(self, a, b):
        """
        a.left = b.right
        a.right = b.left
        a.val = b.val
        """
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return self.symmetric(a.left, b.right) and self.symmetric(a.right, b.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)