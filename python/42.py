class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        lm = [0] * len(height)
        rm = [0] * len(height)
        # Find the max value on the left side
        lm[0] = 0
        for i in range(1, len(height)):
            if height[i-1] > lm[i-1]:
                lm[i] = height[i-1]
            else:
                lm[i] = lm[i-1]
        # Find the max value on the right side
        rm[len(height)-1] = 0
        for i in range(len(height)-2, -1, -1):
            if height[i+1] > rm[i+1]:
                rm[i] = height[i+1]
            else:
                rm[i] = rm[i+1]

        # Trapping water
        water = 0
        for i in range(0, len(height)):
            trap_water = max(min(lm[i], rm[i]) - height[i], 0)
            water += trap_water
        return water

if __name__ == "__main__":
    sol = Solution()
    w = sol.trap([1,0,1])
    print(w)

        