class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, n):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    to_find = target - (nums[i] + nums[j] + nums[k])
                    if to_find in nums[k+1:]:
                        ans.append([nums[i], nums[j], nums[k], to_find])
        return ans

