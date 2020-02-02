# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = len(nums)
        print(nums)
        idx = n // 2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root

def ptree(node):
    if not node:
        return
    buffer = []
    if node.left:
        buffer.append("{} << ".format(node.left.val))
    else:
        buffer.append("NULL << ")
    buffer.append("{} ".format(node.val))
    if node.right:
        buffer.append(">> {}".format(node.right.val))
    else:
        buffer.append(">> NULL")
    print("".join(buffer))
    ptree(node.left)
    ptree(node.right)

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    sol = Solution()
    r = sol.sortedArrayToBST(nums)
    ptree(r)
