# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 1
        cur = head
        while cur.next is not None:
            length += 1
            cur = cur.next
        cur.next = head
        # print("LAST", cur.val, cur.next.val)
        
        offset = k % length
        offset = length-offset
        # print(length, offset, k)
        cnt = 0
        prev = cur
        while cnt != offset:
            prev = head
            head = head.next
            cnt += 1
        prev.next = None
        return head
        
        

if __name__ == "__main__":
    sol = Solution()
    x = ListNode(1)
    y = ListNode(2)
    z = ListNode(3)
    x.next = y
    a = sol.rotateRight(z, 1)
    cur = a
    while cur != None:
        print(cur.val)
        cur = cur.next
