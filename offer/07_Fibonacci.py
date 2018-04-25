# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x

if __name__ == '__main__':
    print Solution().Fibonacci(5)
