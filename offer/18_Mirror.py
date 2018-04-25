# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        left = self.Mirror(root.left)
        right = self.Mirror(root.right)
        root.left = right
        root.right = left
        return root

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().Mirror(root).left.val