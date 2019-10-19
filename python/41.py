class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            cur = nums[i]
            if type(cur) != int:
                continue
            while 0 <= cur-1 < len(nums):
                tmp = nums[cur-1]
                nums[cur-1] = 'Y'
                cur = tmp
                if type(cur) != int:
                    break
        for i in range(len(nums)):
            if type(nums[i]) == int:
                return i+1
        return len(nums)+1