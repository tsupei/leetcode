# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        n = 1
        cur = head
        while cur.next:
            n += 1
            cur = cur.next

        idx = n // 2
        prev = None
        cur = head
        i = 0
        while i != idx:
            i += 1
            prev = cur
            cur = cur.next
        root = TreeNode(cur.val)
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
        if cur.next:
            root.right = self.sortedListToBST(cur.next)
        return root


