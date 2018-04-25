# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right
            left.right, pRootOfTree.left = pRootOfTree, left
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            right.left, pRootOfTree.right = pRootOfTree, right
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(2), TreeNode(1), TreeNode(3)
    s = Solution().Convert(root)
    print s.val, s.right.val, s.right.right.val
