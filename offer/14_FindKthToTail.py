# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0:
            return None
        p = head
        i = 0
        while i < k and p:
            p = p.next
            i += 1
        if i < k:
            return None
        else:
            h = head
            while p:
                h = h.next
                p = p.next
            return h

if __name__ == '__main__':
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    print Solution().FindKthToTail(head, 2).val
