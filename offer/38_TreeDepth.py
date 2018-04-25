# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().TreeDepth(root)


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def depth(root):
#     if root is None:
#         return 0
#     # deep = 1
#     from collections import deque
#     dq = deque()
#     layer = 1
#     dq.append((root, 1))
#     while dq:
#         node, layer = dq.popleft()
#         deep = layer
#         if node.left:
#             dq.append((node.left, layer + 1))
#         if node.right:
#             dq.append((node.right, layer + 1))
#
#     return deep
#
#
# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         return depth(pRoot)