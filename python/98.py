# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def less(self, root, value):
        is_less = True
        if root.left:
            is_less = is_less and self.less(root.left, root.val)
            if not is_less:
                return False
        if root.right:
            is_less = is_less and self.less(root.right, value) and self.greater(root.right, root.val)
            if not is_less:
                return False
        is_less = is_less and (root.val < value)
        return is_less

    def greater(self, root, value):
        is_greater = True
        if root.left:
            is_greater = is_greater and self.greater(root.left, value) and self.less(root.left, root.val)
            if not is_greater:
                return False
        if root.right:
            is_greater = is_greater and self.greater(root.right, root.val)
            if not is_greater:
                return False
        is_greater = is_greater and (root.val > value)
        return is_greater

    def largest(self, node):
        while node.right:
            node = node.right
        return node.val

    def smallest(self, node):
        while node.left:
            node = node.left
        return node.val

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.left:
            if not (self.isValidBST(root.left) and root.left.val < root.val and self.largest(root.left) < root.val):
                return False

        if root.right:
            if not (self.isValidBST(root.right) and root.right.val > root.val and self.smallest(root.right) > root.val):
                return False

        return True


        # is_valid = True
        # if root.left:
        #     is_valid = is_valid and self.less(root.left, root.val)
        #     if not is_valid:
        #         return False
        # if root.right:
        #     is_valid = is_valid and self.greater(root.right, root.val)
        # return is_valid


        