# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def count(self, root):
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.count(root.right) + 1
        if not root.right:
            return self.count(root.left) + 1
        return self.count(root.left) + self.count(root.right) + 1        
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Method 1
        # cur = root        
        # stk = []
        # while cur:
        #     stk.append(cur)
        #     cur = cur.left
        # cnt = 1
        # while stk:
        #     cur = stk.pop()
        #     if cnt == k:
        #         return cur.val
        #     elif cnt < k:
        #         rc = 0
        #         if cur.right:
        #             rc = self.count(cur.right)
        #         if cnt + rc >= k:
        #             return self.kthSmallest(cur.right, k-cnt)
        #         else:
        #             cnt = cnt + rc + 1
        # return -1
        
        # Method 2
        # inorder
        cur = root
        stk = []
        while True:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

