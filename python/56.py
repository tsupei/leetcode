class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort
        intervals = sorted(intervals, key=lambda k: k[0])
        nintervals = []
        cur = 0
        while cur < len(intervals):
            ptr = 0
            upper_bound = intervals[cur][1]
            while cur+ptr+1 < len(intervals) and upper_bound >= intervals[cur+ptr+1][0]:
                upper_bound = upper_bound if intervals[cur+ptr+1][1] < upper_bound else intervals[cur+ptr+1][1]
                ptr += 1
            nintervals.append([intervals[cur][0], upper_bound])
            cur = cur+ptr+1
        return nintervals

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,4],[0,2],[3,5]]
    a = sol.merge(intervals)
    print(a)
