# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 1 << number - 1

if __name__ == '__main__':
    print Solution().jumpFloorII(5)
