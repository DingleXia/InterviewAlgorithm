# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def Root1HasRoot2(pRoot1, pRoot2):
            if pRoot1 is None and pRoot2 is not None:
                return False
            if pRoot2 is None:
                return True
            if pRoot1.val != pRoot2.val:
                return False
            return Root1HasRoot2(pRoot1.left, pRoot2.left) and Root1HasRoot2(pRoot1.right, pRoot2.right)

        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = Root1HasRoot2(pRoot1, pRoot2)
                if not result:
                    return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
                return True
        return False

if __name__ == '__main__':
    r1, r1.left, r1.right = TreeNode(1), TreeNode(2), TreeNode(3)
    r2, r2.left = TreeNode(1), TreeNode(2)
    print Solution().HasSubtree(r1, r2)
