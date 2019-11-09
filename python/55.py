class Solution(object):
    # Solution 1
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return True
        cur_idx = 0
        while True:
            cur_dist = cur_idx + nums[cur_idx]
            max_dist = -1
            max_idx = -1

            for idx, num in enumerate(nums[cur_idx:cur_dist+1]):
                if num + (idx+cur_idx) >= max_dist:
                    max_dist = num + (idx+cur_idx)
                    max_idx = (idx+cur_idx)
            if max_dist >= len(nums) - 1:
                return True
            if max_idx == cur_idx:
                return False
            cur_idx = max_idx


if __name__ == "__main__":
    sol = Solution()
    # Testcase
    # 
    a = sol.canJump([1,0,1,0])
    print(a)




