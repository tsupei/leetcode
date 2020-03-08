class Solution(object):
    def my_combine(self, nums, k):
        if not nums:
            return []
        if k == 1:
            return [[num] for num in nums]
        if len(nums) < k:
            return []
        elif len(nums) == k:
            return [nums]
        else:
            ans = []
            for i in range(len(nums)-k+1):
                combs = self.my_combine(nums[i+1:], k-1)
                for comb in combs:
                    ans.append([nums[i]] + comb)
            return ans
                
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n+1)]
        return self.my_combine(nums, k)
