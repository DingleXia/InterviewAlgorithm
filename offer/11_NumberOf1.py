# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        i = 0
        while n and n >= -2 ** 31:
            i += 1
            n = n & n - 1
        return i

if __name__ == '__main__':
    print Solution().NumberOf1(2)
