# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        def product(array):
            mul = 1
            for a in array:
                mul *= a
            return mul
        B = [0] * len(A)
        for i in range(len(A)):
            B[i] = product(A[:i]) * product(A[i + 1:])
        return B

if __name__ == '__main__':
    print Solution().multiply([1, 2, 3, 4, 5])
