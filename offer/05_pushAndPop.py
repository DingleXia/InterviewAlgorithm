# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.tmp_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
    def pop(self):
        # return xx
        while self.stack:
            self.tmp_stack.append(self.stack.pop())
        elem = self.tmp_stack.pop()

        while self.tmp_stack:
            self.stack.append(self.tmp_stack.pop())
        return elem

if __name__ == '__main__':
    queue = Solution()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.pop()
    print queue.stack
