# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        n = 0
        for i, d in enumerate(data):
            if d == k:
                n += 1
        return n

if __name__ == '__main__':
    print Solution().GetNumberOfK([1, 2, 2, 2, 3, 4, 4], 2)
