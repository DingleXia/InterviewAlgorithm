# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def same(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val is p2.val:
                return same(p1.left, p2.right) and same(p1.right, p2.left)
            return False
        if not pRoot:
            return True
        return same(pRoot.left, pRoot.right)

if __name__ == '__main__':
    r1, r1.left, r1.right = TreeNode(1), TreeNode(2), TreeNode(2)
    print Solution().isSymmetrical(r1)
    r2, r2.left, r2.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().isSymmetrical(r2)