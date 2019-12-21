class Solution(object):
    def subsetsWithDubSorted(self, nums):
        if not nums:
            return [[]]
        arr = []
        cur = nums[0]
        cnt = 1

        # O(n) >> Repeated count
        for num in nums[1:]:
            if num == cur:
                cnt += 1
            else:
                break
        subs = self.subsetsWithDubSorted(nums[cnt:])
        for sub in subs:
            for c in range(cnt+1):
                arr.append([cur] * c + sub)
        return arr


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums = sorted(nums)
        return self.subsetsWithDubSorted(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,2,2]
    ans = sol.subsetsWithDup(nums)
    print(ans)
