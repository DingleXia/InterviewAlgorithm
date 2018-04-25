# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for a in array:
            if a & 1:
                odd.append(a)
            else:
                even.append(a)
        return odd + even

if __name__ == '__main__':
    print Solution().reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9])