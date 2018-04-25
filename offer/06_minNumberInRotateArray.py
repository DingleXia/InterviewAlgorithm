# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        min = float('inf')
        for num in rotateArray:
            if num < min:
                min = num
        return min

if __name__ == '__main__':
    rotateArray = [3, 4, 5, 1, 2]
    print Solution().minNumberInRotateArray(rotateArray)
