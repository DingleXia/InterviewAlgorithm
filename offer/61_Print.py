# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        res = []
        tmp = []
        end = pRoot
        reverse = False
        while queue:
            t = queue.pop(0)
            tmp.append(t.val)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
            if t == end:
                if not reverse:
                    res.append(tmp)
                else:
                    res.append(tmp[::-1])
                reverse = not reverse
                tmp = []
                if queue:
                    end = queue[-1]
        return res

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right = TreeNode(4), TreeNode(5)
    print Solution().Print(root)
