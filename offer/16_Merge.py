# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            head = pHead1
            pHead1 = pHead1.next
        else:
            head = pHead2
            pHead2 = pHead2.next
        p = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                p = p.next
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                p = p.next
                pHead2 = pHead2.next
        if pHead1 is None:
            p.next = pHead2
        else:
            p.next = pHead1
        return head

if __name__ == '__main__':
    h1, h1.next = ListNode(1), ListNode(2)
    h2, h2.next = ListNode(2), ListNode(3)
    m = Solution().Merge(h1, h2)
    print m.val
    print m.next.val
    print m.next.next.val
    print m.next.next.next.val
