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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        tmp = []
        cur = head
        prev = None
        found = False
        while cur:
            if prev:
                prev.next = cur
            if cur.val < x:
                if prev is None:
                    head = cur
                prev = cur
            else:
                tmp.append(cur)
            cur = cur.next
        if prev:
            prev.next = cur

        if prev is None:
            # Check is new heas is assigned
            cur = None
        else:
            # Walk through to the last node
            cur = head
            while cur.next is not None:
                cur = cur.next
        for node in tmp:
            if cur is None:
                head = node
            else:
                cur.next = node
            cur = node
        cur.next = None
        return head

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c


    sol = Solution()
    ans = sol.partition(a, 2)
    sol.pprint(ans)
