# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        array = []
        p = pHead
        while p:
            if p in array:
                return p
            else:
                array.append(p)
            p = p.next
        return None

if __name__ == '__main__':
    head, head.next, head.next.next, head.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    head.next.next.next.next = head.next
    print Solution().EntryNodeOfLoop(head).val

