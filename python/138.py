"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        # Copy val and next 
        cp_head = Node(x=head.val)
        cp_ptr = cp_head
        cur = head
        while cur.next:
            cp_next = Node(x=cur.next.val)
            cp_ptr.next = cp_next
            cp_ptr = cp_next
            cur = cur.next
        # Copy Random
        # O(n^2)
        cur = head
        cp_ptr = cp_head
        while cur:
            target = cur.random
            if target:
                sub_cur = head
                sub_cp_ptr = cp_head
                while sub_cur != target:
                    sub_cur = sub_cur.next
                    sub_cp_ptr = sub_cp_ptr.next
                cp_ptr.random = sub_cp_ptr
            else:
                cp_ptr.random = None
            cp_ptr = cp_ptr.next
            cur = cur.next
        return cp_head
