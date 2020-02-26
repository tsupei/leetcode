class Solution(object):
    def binary_search(self, nums, offset):
        if not nums:
            # 不會出現的情況
            return -1
        if len(nums) == 1:
            return offset
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return offset
            else:
                return offset + 1
        mid = len(nums) // 2
        if nums[mid-1] <= nums[mid] and nums[mid+1] <= nums[mid]:
            return mid + offset
        if nums[mid-1] >= nums[mid]:
            return self.binary_search(nums[:mid], offset)
        if nums[mid+1] >= nums[mid]:
            return self.binary_search(nums[mid+1:], offset+mid+1)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            # 不會出現的情況
            return -1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        return self.binary_search(nums, 0)


