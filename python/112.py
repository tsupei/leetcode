# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # method 2: For loop
        if not root:
            return False
        stack = [(root, sum)]
        while stack:
            cur, cur_sum = stack.pop()
            if cur_sum == cur.val:
                if not cur.left and not cur.right:
                    # A leaf node
                    return True
            if cur.left:
                stack.append((cur.left, cur_sum-cur.val))
            if cur.right:
                stack.append((cur.right, cur_sum-cur.val))
        return False
            
