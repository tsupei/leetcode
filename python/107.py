# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        if not root.left:
            lt = []
        else:
            lt = self.levelOrderBottom(root.left)
        if not root.right:
            rt = []
        else:
            rt = self.levelOrderBottom(root.right)
        ldep = len(lt)
        rdep = len(rt)
        t = []
        if rdep > ldep:
            offset = rdep - ldep
            t.extend(rt[:offset])
            for i in range(ldep):
                t.append(lt[i]+rt[offset+i])
        else:
            offset = ldep - rdep
            t.extend(lt[:offset])
            for i in range(rdep):
                t.append(lt[offset+i]+rt[i])
        t.append([root.val])
        return t

if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    sol = Solution()
    ans = sol.levelOrderBottom(a)
    print(ans)
