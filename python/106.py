# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        root = postorder[-1]
        root_idx = -1
        for idx, node in enumerate(inorder):
            if node == root:
                root_idx = idx
                break
        root_node = TreeNode(root)
        root_node.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root_node.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
        return root_node