class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy
        if len(nums) == 1:
            return 0
        step = 0
        cur = 0
        while True:
            max_dist = -1
            max_idx = -1
            # print("---")
            # print(cur)
            # print(step)
            # print(nums[cur+1:cur+nums[cur]+1])
            if nums[cur] + cur  >= len(nums)-1:
                return step+1
            for idx, tag in enumerate(nums[cur+1:cur+nums[cur]+1]):
                if cur+idx+tag >= max_dist:
                    max_dist = cur+1+idx+tag
                    max_idx = cur+1+idx
            step += 1
            cur = max_idx
            if max_dist >= len(nums) - 1:
                return step+1

if __name__ == "__main__":
    sol = Solution()
    # Testcase
    # 
    a = sol.jump([3,1,2])
    print(a)