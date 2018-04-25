# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        x, y = 1, 1
        for i in range(number):
            x, y = y, x + y
        return x

if __name__ == '__main__':
    print Solution().jumpFloor(5)
