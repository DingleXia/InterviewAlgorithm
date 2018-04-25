# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            left=pNode.right
            while left.left:
                   left = left.left
            return left
        p = pNode
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp

if __name__ == '__main__':
    root, root.left, root.right = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3)
    root.next, root.left.next, root.right.next = None, root, root
    print Solution().GetNext(root).val
    print Solution().GetNext(root.left).val
    print Solution().GetNext(root.right)