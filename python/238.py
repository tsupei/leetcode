class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1 = [1]
        tmp = 1
        for num in nums[::-1]:
            tmp *= num
            nums1.append(tmp)
        nums1.pop()
        nums1 = nums1[::-1]
        nums2 = [1]
        tmp = 1
        for num in nums:
            tmp *= num
            nums2.append(tmp)
        nums2.pop()
        for i in range(len(nums)):
            nums[i] = nums1[i] * nums2[i]
        return nums
