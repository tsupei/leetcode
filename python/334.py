class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        tmp = None
        pptr = None
        ptr = 0
        for i in range(1, len(nums)):
            # print(tmp, pptr, ptr)
            if nums[i] <= nums[ptr]:
                if pptr is not None:
                    if nums[i] > nums[pptr]:
                        ptr = i
                    else:
                        if tmp is None:
                            tmp = i
                        else:
                            if nums[i] > nums[tmp]:
                                ptr = i
                                pptr = tmp
                else:
                    ptr = i
            else:
                if pptr is not None:
                    return True
                pptr = ptr
                ptr = i
        return False

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,-10,-8,-7]
    ans = sol.increasingTriplet(nums)
    print(ans)
