# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, root):
        if not root:
            return True, 0
        lb, lh = self.height(root.left)
        rb, rh = self.height(root.right)
        if abs(lh-rh) <= 1 and lb and rb:
            return True, max(lh, rh) + 1
        else:
            return False, -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        is_balanced, _ = self.height(root)
        return is_balanced
