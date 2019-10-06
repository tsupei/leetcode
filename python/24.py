# Definition for singly-linked list.
# n = length of linked list
# O(n)
# 將所有的元素按照單雙存成兩個list
# 再反向存回去

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # margin testcase
        if not head:
            return None
        if not head.next:
            return head
        order_list_1 = []
        order_list_2 = []
        cur = head
        cur_idx = 0
        while cur:
            if cur_idx % 2 == 0:
                order_list_1.append(cur)
            else:
                order_list_2.append(cur)
            cur = cur.next
            cur_idx += 1
        min_len = min(len(order_list_1), len(order_list_2))
        ans_head = ans_cur = order_list_2[0]
        ans_cur.next = order_list_1[0]
        ans_cur = ans_cur.next
        for i in range(1, min_len):
            ans_cur.next = order_list_2[i]
            ans_cur = ans_cur.next
            ans_cur.next = order_list_1[i]
            ans_cur = ans_cur.next
        if len(order_list_1) == min_len+1:
            ans_cur.next = order_list_1[min_len]
            ans_cur = ans_cur.next
        ans_cur.next = None
        ans_cur = ans_head
        # while ans_cur:
        #     print(ans_cur.val)
        #     ans_cur = ans_cur.next
        return ans_head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    t = ListNode(2)
    tt = ListNode(3)
    ttt = ListNode(4)
    head.next = t
    t.next = tt
    tt.next = ttt
    sol.swapPairs(head)