# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def path(self, root, x):
        if not root:
            return []
        if root == x:
            return [root]
        if root.right:
            rp = self.path(root.right, x)
            if rp:
                rp = [root] + rp
                return rp
        if root.left:
            lp = self.path(root.left, x)
            if lp:
                lp = [root] + lp
                return lp
        return []
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pp = self.path(root, p) # path of p
        pq = self.path(root, q) # path of q
        # print([e.val for e in pp])
        # print([e.val for e in pq])
        lca = root
        for i in range(1, min(len(pp), len(pq))):
            if pp[i] != pq[i]:
                return lca
            else:
                lca = pp[i]
        return lca


 
