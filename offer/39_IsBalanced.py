# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def DeepTree(pRoot):
            if not pRoot:
                return 0
            return max(DeepTree(pRoot.left), DeepTree(pRoot.right)) + 1
        if not pRoot:
            return True
        leftDeep = DeepTree(pRoot.left)
        rightDeep = DeepTree(pRoot.right)
        if abs(leftDeep - rightDeep) > 1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().IsBalanced_Solution(root)
