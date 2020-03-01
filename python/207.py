class Solution(object):
    def walk(self, v, g, s, c):
        # v: record visited points
        # g: graph
        # s: start point
        # c: current point
        v[c] = True
        print(s,c)
        if g[c]:
            for p in g[c]:
                if not v[p]:
                    if not self.walk(v, g, s, p):
                        return False
                else:
                    if p == s:
                        return False
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for target, pre in prerequisites:
            graph[target].append(pre)
        # If a loop exist, then invalid
        for i in range(numCourses):
            v = [False] * numCourses
            if not self.walk(v, graph, i, i):
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[0,1],[3,1],[1,3],[3,2]]
    res = sol.canFinish(numCourses, prerequisites)
    print(res)
