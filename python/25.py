# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def reverse_next(node):
    if node.next:
        next_node = node.next
        next_node, head = reverse_next(next_node)
        next_node.next = node
        node.next = None
        return node, head
    else:
        return node, node

def reverse(head):
    tail, head = reverse_next(head)
    return tail, head

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # margin testcase
        if k == 1:
            return head
        if not head:
            return None
        cur = head
        sol_head = None
        prev_tail = None
        while cur:
            counter = 1
            tmp_head = cur
            while counter < k and cur:
                cur = cur.next
                counter += 1
            if cur:
                tmp = cur
                cur = cur.next
                tmp.next = None
                tail, head = reverse(tmp_head)
                if not sol_head:
                    sol_head = head
                if prev_tail:
                    prev_tail.next = head
                prev_tail = tail
            else:
                if not prev_tail:
                    sol_head = head
                else:
                    prev_tail.next = tmp_head
                break
        return sol_head

if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    sol = Solution()
    head = sol.reverseKGroup(head, 3)
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
