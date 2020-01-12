# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def find_max(self, root, maximum, max_node):
        if not root:
            return maximum, max_node
        if root.val > maximum:
            maximum = root.val
            max_node = root

        left_max, left_max_node = self.find_max(root.left, maximum, max_node)
        right_max, right_max_node = self.find_max(root.right, maximum, max_node)
        if left_max > right_max:
            return left_max, left_max_node
        else:
            return right_max, right_max_node

    def find_min(self, root, minimum, min_node):
        if not root:
            return minimum, min_node
        if root.val < minimum:
            minimum = root.val
            min_node = root

        left_min, left_min_node = self.find_min(root.left, minimum, min_node)
        right_min, right_min_node = self.find_min(root.right, minimum, min_node)
        if left_min < right_min:
            return left_min, left_min_node
        else:
            return right_min, right_min_node

    def left_max(self, root):
        cur = root.left
        if not cur:
            return None
        while cur.right:
            cur = cur.right
        return cur.val

    def right_min(self, root):
        cur = root.right
        if not cur:
            return None
        while cur.left:
            cur = cur.left
        return cur.val


    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if not root.left and not root.right:
            return

        if not root.left or root.val > self.left_max(root):
            if not root.right or root.val < self.right_min(root):
                self.recoverTree(root.left)
                self.recoverTree(root.right)
            else:
                # Right Tree
                right_min, right_min_node = self.find_min(root.right, root.right.val, root.right)
                if right_min < root.val:
                    # Swapping
                    right_min_node.val = root.val
                    root.val = right_min
                else:
                    # Error
                    print("ERROR")
        else:
            if not root.right or root.val < self.right_min(root):
                # Left Tree
                left_max, left_max_node = self.find_max(root.left, root.left.val, root.left)

                if left_max > root.val:
                    # Swapping
                    left_max_node.val = root.val
                    root.val = left_max
                else:
                    # Error
                    print("ERROR")
            else:
                
            


