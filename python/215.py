class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sort: O(nlgn)
        nums = sorted(nums, reverse=True)
        return nums[k-1]
