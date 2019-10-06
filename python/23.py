import time
# Time Complexity
# m = length of lists
# n = longest list length
# O(mn)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        flag = True
        ans_head, ans_cur = None, None

        while flag:
            flag = False
            min_val, min_idx = None, -1
            move_idx = []
            for idx, list_node in enumerate(lists):
                # if list_node:
                #     print("{}: {}".format(idx, list_node.val))
                # else:
                #     print("{}: end".format(idx))
                if (list_node and min_idx == -1) or (list_node and list_node.val < min_val):
                    min_val= list_node.val
                    min_idx = idx
                    move_idx = [idx]
                    flag = True
            if flag:
                for idx in range(len(lists)):
                    while lists[idx] and lists[idx].val <= min_val:
                        # if lists[idx]:
                        #     print("{}: {}".format(idx, lists[idx].val))
                        # else:
                        #     print("{}: end".format(idx))
                        if ans_cur:
                            ans_cur.next = lists[idx]
                            ans_cur = lists[idx]
                        else:
                            ans_head = ans_cur = lists[idx]
                        lists[idx] = lists[idx].next
        # ans_cur = ans_head
        # while ans_cur:
        #     print(ans_cur.val)
        #     ans_cur = ans_cur.next
        return ans_head
# 1->4->5,
#   1->3->4,
#   2->6
if __name__ == "__main__":
    sol = Solution()
    a1,a2,a3 = ListNode(1),ListNode(4),ListNode(5)
    b1,b2,b3 = ListNode(1),ListNode(3),ListNode(4)
    c1,c2 = ListNode(2), ListNode(6)
    a1.next = a2
    a2.next = a3
    b1.next = b2
    b2.next = b3
    c1.next = c2
    sol.mergeKLists([a1, b1, c1])
