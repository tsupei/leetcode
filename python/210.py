class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Greedy
        path = []
        
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
                path.append(cand)
            cands = []
            for k, v in graph.items():
                if taken[k] == 0:
                    for prerequisite in v:
                        if taken[prerequisite] != 1:
                            break
                    else:
                        cands.append(k)
        if sum(taken) != numCourses:
            return []
        return path
