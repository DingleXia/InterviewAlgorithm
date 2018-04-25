# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == target:
                    return True
        return False

if __name__ == '__main__':
    array = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [6, 7, 8, 9]
    ]
    print Solution().Find(6, array)