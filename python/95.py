# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTreesOffset(self, n, offset):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(1+offset)]
        nodes = []
        for root in range(1, n+1):
            print(n, root, offset)
            left_nodes = self.generateTreesOffset(root-1, offset)
            right_nodes = self.generateTreesOffset(n-root, root+offset)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root_node = TreeNode(root+offset)
                    root_node.left = left_node
                    root_node.right = right_node
                    nodes.append(root_node)
        return nodes
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesOffset(n, 0)

def vis(node, level):
    if not node:
        print("".join(["\t"] * level + ["null"]))
        return
    vis(node.left, level+1)
    print("".join(["\t"] * level + [str(node.val)]))
    vis(node.right, level+1)


if __name__ == "__main__":
    sol = Solution()
    nodes = sol.generateTrees(3)
    print(nodes)
    for node in nodes:
        print("--")
        vis(node, 0)