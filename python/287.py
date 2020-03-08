class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = 0
        hare = 0
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise

