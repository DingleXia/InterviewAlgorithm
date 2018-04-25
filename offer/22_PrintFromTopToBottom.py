# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        array = []
        queue = []
        queue.append(root)
        while queue:
            t = queue.pop(0)
            array.append(t.val)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
        return array

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().PrintFromTopToBottom(root)