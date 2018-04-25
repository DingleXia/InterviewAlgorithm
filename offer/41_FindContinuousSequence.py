# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        array = []
        for i in range(1, tsum + 1):
            for j in range(i + 1, tsum + 1):
                if (i + j) * (j - i + 1) == 2 * tsum:
                    array.append([_ for _ in range(i, j + 1)])
        return array

if __name__ == '__main__':
    print Solution().FindContinuousSequence(100)

