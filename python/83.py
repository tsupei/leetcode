# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def print_list(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    sol = Solution()
    ans = sol.deleteDuplicates(a)
    sol.print_list(ans)

