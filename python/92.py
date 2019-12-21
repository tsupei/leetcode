# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def pprint(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            nptr = cur.next
            cur.next = prev
            prev = cur
            cur = nptr
        return prev, head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        ptr1 = head
        i = 1
        prev = None
        while i < m:
            prev = ptr1
            ptr1 = ptr1.next
            i += 1
        rec1 = prev
        ptr2 = ptr1
        while i < n:
            ptr2 = ptr2.next
            i += 1
        rec2 = ptr2.next
        ptr2.next = None

        # Reverse
        sub_head, sub_tail = self.reverse(ptr1)

        # Insert
        if rec1:
            rec1.next = sub_head
            sub_tail.next = rec2
            return head
        else:
            sub_tail.next = rec2
            return sub_head
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    sol = Solution()
    ans = sol.reverseBetween(a, 1,5)
    sol.pprint(ans)

















