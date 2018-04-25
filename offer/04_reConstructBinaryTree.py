# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre:
            try:
                rindex = tin.index(pre[0])
            except Exception, e:
                print e.message
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:rindex + 1], tin[:rindex])
            root.right = self.reConstructBinaryTree(pre[rindex + 1:], tin[rindex + 1:])
            return root
        return None

if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    print Solution().reConstructBinaryTree(pre, tin).val
