class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Greedy
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for to_node, from_node in prerequisites:
            graph[to_node].append(from_node)
            
        cands = []
        for k, v in graph.items():
            if not v:
                cands.append(k)
        
        taken = [0] * numCourses
        while cands:
            for cand in cands:
                taken[cand] = 1
            cands = []
            for k, v in graph.items():
                if taken[k] == 0:
                    for prerequisite in v:
                        if taken[prerequisite] != 1:
                            break
                    else:
                        cands.append(k)
        if sum(taken) != numCourses:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]] 
    res = sol.canFinish(numCourses, prerequisites)
    print(res)
