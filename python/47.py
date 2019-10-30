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
        prev = None
        for i in range(0, len(nums)):
            if prev != None:
                if nums[i] == prev:
                    continue
            prev = nums[i]
            others = self.permute(nums[:i]+nums[i+1:])
            for other in others:
                pers.append([nums[i]]+other)
        return pers

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        return self.permute(nums)

if __name__ == "__main__":
    sol = Solution()
    ans = sol.permuteUnique([0,1,0,0,9])
    print(ans)