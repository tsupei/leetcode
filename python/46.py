class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
        	return []
        if len(nums) == 1:
        	return [nums]
        pers = []
        for i in range(len(nums)):
            others = self.permute(nums[:i]+nums[i+1:])
            for other in others:
                pers.append([nums[i]]+other)
        return pers


if __name__ == "__main__":
    sol = Solution()
    ans = sol.permute([1,2,3,4])
    print(ans)