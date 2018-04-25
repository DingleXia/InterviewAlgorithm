# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        p = None
        while stack1[-1].val == stack2[-1].val:
            p = stack1[-1]
            stack1.pop()
            stack2.pop()
        return p

if __name__ == '__main__':
    common, common.next = ListNode(4), ListNode(5)
    h1, h1.next, h1.next.next = ListNode(1), ListNode(2), common
    h2, h2.next, h2.next.next = ListNode(1), ListNode(3), common
    print Solution().FindFirstCommonNode(h1, h2).val

