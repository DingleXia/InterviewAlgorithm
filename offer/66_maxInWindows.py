# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0:
            return []
        res = []
        for i in xrange(0, len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res

if __name__ == '__main__':
    print Solution().maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
