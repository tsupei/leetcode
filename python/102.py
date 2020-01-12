# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        # === Recursive Solution ===

        # levels = [[root.val]]

        # left_levels = self.levelOrder(root.left)
        # right_levels = self.levelOrder(root.right)

        # n = len(left_levels)
        # m = len(right_levels)

        # for i in range(max(n, m)):
        #     if i >= n:
        #         left = []
        #     else:
        #         left = left_levels[i]
        #     if i >= m:
        #         right = []
        #     else:
        #         right = right_levels[i]
        #     levels.append(left + right)
        # return levels

        # === Loop Solution ===

        # left go
        levels = [[root.val]]
        queue = [root.left, root.right]
        while queue:
            level = []
            nqueue = []
            for ele in queue:
                if ele:
                    level.append(ele.val)
                    nqueue.append(ele.left)
                    nqueue.append(ele.right)
            if level:
                levels.append(level)
            queue = nqueue
        return levels


