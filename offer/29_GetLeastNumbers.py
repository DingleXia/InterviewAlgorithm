# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k <= 0 or k > len(tinput):
            return []
        n = sorted(tinput)
        return n[:k]

if __name__ == '__main__':
    print Solution().GetLeastNumbers_Solution([9, 8, 7, 6, 5, 4, 3, 2, 1], 4)


