# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
        if not self.stack2:
            self.stack2.append(node)
        elif node < self.stack2[-1]:
            self.stack2.append(node)
        else:
            self.stack2.append(self.stack2[-1])
    def pop(self):
        # write code here
        self.stack2.pop()
        return self.stack1.pop()

    def top(self):
        # write code here
        return self.stack1[-1]
    def min(self):
        # write code here
        return self.stack2[-1]

if __name__ == '__main__':
    stack = Solution()
    stack.push(1)
    stack.push(2)
    print stack.min()
