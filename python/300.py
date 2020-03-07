class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        for i in range(len(nums)):
            pptr = None
            ptr = nums[i]
            length = 1
            for j in range(i+1, len(nums)):
                # print(pptr, ptr)
                if nums[j] > ptr:
                    pptr = ptr
                    ptr = nums[j]
                    length += 1
                else:
                    if pptr is not None and nums[j] > pptr:
                        ptr = nums[j]
            if length > max_len:
                max_len = length
        return max_len

if __name__ == "__main__":
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    ans = sol.lengthOfLIS(nums)
    print(ans)
