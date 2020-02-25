# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # Use the first node as pivot
        pivot = head
        cur = head.next

        # Maintain 3 Linked List
        smaller_head = None
        smaller_ptr = None
        eq_head = pivot
        eq_ptr = pivot
        bigger_head = None
        bigger_ptr = None
        while cur:
            if pivot.val > cur.val:
                if not smaller_head:
                    smaller_head = cur
                    smaller_ptr = cur
                else:
                    smaller_ptr.next = cur
                    smaller_ptr = cur
            elif pivot.val == cur.val:
                eq_ptr.next = cur
                eq_ptr = cur
            else:
                if not bigger_head:
                    bigger_head = cur
                    bigger_ptr = cur
                else:
                    bigger_ptr.next = cur
                    bigger_ptr = cur
            cur = cur.next
        # Ensure tail.next points to NULL
        if smaller_ptr:
            smaller_ptr.next = None
        if bigger_ptr:
            bigger_ptr.next = None
        eq_ptr.next = None

        smaller_head = self.sortList(smaller_head)
        bigger_head = self.sortList(bigger_head)

        # if there are no smaller elements, then we got into a bad situation, which means O(n)
        if smaller_head:
            smaller_ptr = smaller_head
            while smaller_ptr.next:
                smaller_ptr = smaller_ptr.next
            smaller_ptr.next = eq_head
            eq_ptr.next = bigger_head
            return smaller_head
        else:
            eq_ptr.next = bigger_head
            return eq_head
