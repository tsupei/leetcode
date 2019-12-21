class Solution(object):
    def searchRectangleAread(self, mi, mv, heights):
        lptr = mi  # left pointer
        rptr = mi  # right pointer
        max_area = 0  
        cur_height = mv
        while lptr >= 0 and rptr < len(heights):
            area = (rptr - lptr + 1) * cur_height
            # print(area, lptr, rptr, cur_height)
            if area > max_area:
                max_area = area
            if lptr == 0:
                rptr += 1
                if rptr < len(heights):
                    cur_height = min(cur_height, heights[rptr])
                continue
            if rptr == len(heights)-1:
                lptr -= 1
                if lptr >= 0:
                    cur_height = min(cur_height, heights[lptr])
                continue

            if heights[lptr-1] > heights[rptr+1]:
                lptr -= 1
                cur_height = min(cur_height, heights[lptr])
            else:
                rptr += 1
                cur_height = min(cur_height, heights[rptr])
            # Pruning
            if cur_height == 0:
                break
        return max_area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # Find the maximum: O(n)
        if not heights:
            return 0
        mv = heights[0]  # max value
        mi = 0  # max index
        max_area = 0
        idx = 0
        flag = True 
        for idx in range(len(heights)):
            prev_height = 0 if idx-1 < 0 else heights[idx-1]
            next_height = 0 if idx+1 >= len(heights) else heights[idx+1]
            if heights[idx] > prev_height and heights[idx] > next_height:
                area = self.searchRectangleAread(idx, heights[idx], heights)
                if area > max_area:
                    max_area = area
            elif heights[idx] >= prev_height and heights[idx] >= next_height and flag:
                area = self.searchRectangleAread(idx, heights[idx], heights)
                flag = False
                if area > max_area:
                    max_area = area
            else:
                flag = True

        return max_area



if __name__ == "__main__":
    sol = Solution()
    heights = [1,1]
    print(heights)

    area = sol.largestRectangleArea(heights)
    print(area)
