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
        prev = None
        rec = []
        while cur:
            if cur.next and cur.val == cur.next.val :
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next  
                if not prev:
                    head = cur.next
                    prev = None
                    cur = cur.next              
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head


        
if __name__ == "__main__":
    aa = ListNode(1)
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(3)
    dd = ListNode(3)
    aa.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = dd
    sol = Solution()
    ans = sol.deleteDuplicates(aa)
    sol.print_list(ans)