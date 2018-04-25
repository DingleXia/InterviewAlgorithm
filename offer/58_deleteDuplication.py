# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        p = pHead
        q = p.next
        if q.val != p.val:
            p.next = self.deleteDuplication(q)
        else:
            while q is not None and p.val == q.val:
                q = q.next
            if not q:
                return None
            else:
                p = self.deleteDuplication(q)
        return p

if __name__ == '__main__':
    head, head.next, head.next.next, head.next.next.next = ListNode(1), ListNode(2), ListNode(2), ListNode(4)
    h = Solution().deleteDuplication(head)
    print h.val, h.next.val, h.next.next
