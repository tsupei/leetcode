# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head2 = head.next
        cur = head
        ptr = head.next
        
        while ptr:
            cur.next = ptr.next
            cur = ptr
            ptr = ptr.next
        
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = head2
        return head


