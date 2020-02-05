# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # if not root.left and root.right:
        #     return self.minDepth(root.right) + 1
        # if not root.right and root.left:
        #     return self.minDepth(root.left)
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # Solution 2
        if not root:
            return 0
        minima = -1
        q = [(root, 1)]
        while q:
            cur, level = q.pop()
            if not cur.left and not cur.right:
                if minima == -1:
                    minima = level
                else:
                    minima = min(minima, level)
            if cur.left:
                q.append((cur.left, level+1))
            if cur.right:
                q.append((cur.right, level+1))
        return minima

