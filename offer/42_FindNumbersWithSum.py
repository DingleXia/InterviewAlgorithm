# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        arr = []
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == tsum:
                    arr.append([array[i], array[j]])
        if not arr:
            return []
        product = [[a[0], a[1], a[0] * a[1]] for a in arr]
        pmin = [0, 0, float('inf')]
        for p in product:
            if p[2] < pmin[2]:
                pmin = p
        return [pmin[0], pmin[1]]

if __name__ == '__main__':
    print Solution().FindNumbersWithSum([1, 2, 3, 4, 5, 6], 6)