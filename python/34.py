class Solution(object):
    def binary_search(self, nums, target, offset):
        if not nums:
            return -1, -1
        mid = int(len(nums)/2)
        if target < nums[mid]:
            return self.binary_search(nums[:mid], target, offset)
        elif target > nums[mid]:
            return self.binary_search(nums[mid+1:], target, offset+mid+1)
        else:
            first = mid
            for i in range(mid, -1, -1):
                if target == nums[i]:
                    first = i
                else:
                    break
            last = mid
            for i in range(mid+1, len(nums)):
                if target == nums[i]:
                    last = i
                else:
                    break
            return first+offset, last+offset

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.binary_search(nums, target, 0)


if __name__ == "__main__":
    sol = Solution()
    nums =[2, 2]
    target = 2
    first, last = sol.searchRange(nums, target)
    print(first, last)


