# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 第三个节点是4
        # 前序遍历5324768
        # 中序遍历2345678
        # 后序遍历2436875
        # 所以是中序遍历，左根右
        global result
        result = []
        self.midnode(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k - 1]

    def midnode(self, root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)

if __name__ == '__main__':
    root, root.left, root.right = TreeNode(2), TreeNode(1), TreeNode(3)
    print Solution().KthNode(root, 1).val
    print Solution().KthNode(root, 2).val
    print Solution().KthNode(root, 3).val
