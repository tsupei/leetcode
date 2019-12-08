class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        cnt = 0
        ptr = 0
        for num in nums:
            nums[ptr] = num
            if prev is None or num == prev:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                ptr += 1
            prev = num
        return ptr



if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(nums)
    ptr = sol.removeDuplicates(nums)
    print(nums, ptr)