class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cur] = nums[i]
                cur += 1
                cnt += 1
        return cnt

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,2,3]
    leng = sol.removeElement(nums, 2)
    print(leng, nums)