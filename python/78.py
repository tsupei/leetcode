class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        comb = []
        subs = self.subsets(nums[1:])
        for sub in subs:
            comb.append([nums[0]] + sub)
            comb.append(sub)
        return comb



if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    ans = sol.subsets(nums)
    print(ans)