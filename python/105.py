# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # [3, 9, 1, 2, 20, 15, 7]
        # [1, 9, 2, 3, 15, 20, 7]
        if not preorder or not inorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = preorder[0]
        root_idx = -1
        for idx, node in enumerate(inorder):
            if node == root:
                root_idx = idx
                break            
        root_node = TreeNode(root)
        root_node.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root_node.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root_node