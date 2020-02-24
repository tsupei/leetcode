"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        if not root.left:
            return root
        lt = root.left # left tree
        rt = root.right # right tree
        while lt:
            lt.next = rt
            lt = lt.right
            rt = rt.left
        root.left = self.connect(root.left)
        root.right = self.connect(root.right)
        return root



