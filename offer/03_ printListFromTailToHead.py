# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        def printListFromTailToHeadRecursively(array, listNode):
            if listNode is None:
                return
            else:
                printListFromTailToHeadRecursively(array, listNode.next)
                array.append(listNode.val)

        array = []
        printListFromTailToHeadRecursively(array, listNode)
        return array

if __name__ == '__main__':
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    print Solution().printListFromTailToHead(head)