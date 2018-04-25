# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        h = ListNode(0)
        p = h
        for i in range(1, n):
            p.next = ListNode(i)
            p = p.next
        p.next = h
        while h != h.next:
            for i in range(1, m):
                p = p.next
                h = h.next
            h = h.next
            p.next = h
        return h.val

if __name__ == '__main__':
    print Solution().LastRemaining_Solution(10, 5)