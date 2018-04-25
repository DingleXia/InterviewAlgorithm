# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while j < len(popV) and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        return True if len(stack) == 0 else False

if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [5, 4, 3, 2, 1]
    print Solution().IsPopOrder(pushV, popV)
