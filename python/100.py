# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        res = True
        if not p.left and not q.left:
            res = res and True
        else:
            res = res and self.isSameTree(p.left, q.left)
        if not p.right and not p.left:
            res = res and True
        else:
            res = res and self.isSameTree(p.right, q.right)

        return res