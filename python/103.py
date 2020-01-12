# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        levels = [[root.val]]
        queue = [root.left, root.right]
        dep = 2
        while queue:
            level = []
            nqueue = []
            for ele in queue:
                if ele:
                    level.append(ele.val)
                    nqueue.append(ele.left)
                    nqueue.append(ele.right)
            if level:
                if dep % 2 == 0:
                    levels.append(level[::-1])
                else:
                    levels.append(level)
            dep += 1
            queue = nqueue
        return levels