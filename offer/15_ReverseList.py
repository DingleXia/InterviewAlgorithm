# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        pre = None
        cur = pHead
        nex = pHead.next
        if not nex:
            return cur
        while nex:
            cur.next = pre
            pre = cur
            cur = nex
            nex = cur.next
        cur.next = pre
        return cur

if __name__ == '__main__':
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    print Solution().ReverseList(head).val
