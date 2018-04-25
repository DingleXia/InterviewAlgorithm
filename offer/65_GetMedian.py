# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self):
        # write code here
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length / 2] + self.data[length / 2 - 1]) / 2.0
        else:
            return self.data[int(length / 2)]

if __name__ == '__main__':
    s = Solution()
    s.Insert(5)
    s.Insert(1)
    s.Insert(7)
    s.Insert(2)
    s.Insert(6)
    s.Insert(9)
    s.Insert(4)
    s.Insert(8)
    s.Insert(3)
    print s.GetMedian()