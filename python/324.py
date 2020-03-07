class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        n = len(nums) // 2
        if len(nums) % 2 == 1:
            n += 1
        for i in range(n):
            nums[i*2] = sorted_nums[n-1-i]
            if 2*i+1 < len(nums):
                nums[i*2+1] = sorted_nums[len(nums)-1-i]


