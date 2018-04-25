# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        x, y = 1, 1
        for i in range(number):
            x, y = y, x + y
        return x

if __name__ == '__main__':
    print Solution().rectCover(5)
