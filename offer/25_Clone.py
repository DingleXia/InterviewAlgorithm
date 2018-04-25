# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        def searchP(p, label):
            if not p:
                return None
            while p:
                if p.label == label:
                    return p
                p = p.next
            return None
        if not pHead:
            return None
        p = pHead
        h = RandomListNode(p.label)
        q = h
        p = p.next
        while p:
            q.next = RandomListNode(p.label)
            p = p.next
            q = q.next
        p = pHead
        q = h
        while p:
            if not p.random:
                q.random = None
            else:
                q.random = searchP(h, p.random.label)
            p = p.next
            q = q.next
        return h

if __name__ == '__main__':
    head, head.next, head.next.next = RandomListNode(1), RandomListNode(2), RandomListNode(3)
    head.random = head.next.next
    head.next.random = head.next.next
    print Solution().Clone(head).random.label

