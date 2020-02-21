# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        while cur:
            if not cur.val:
                return True
            ncur = cur.next
            cur.val = None
            cur = ncur
        return False

