class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur = 1
        last_num = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != last_num:
                last_num = nums[i]
                nums[cur] = nums[i]
                cur += 1
                cnt += 1
        return cnt

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,2,3]
    leng = sol.removeDuplicates(nums)
    print(leng, nums)