# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        k = i
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        left = sequence[:k]
        right = sequence[k:len(sequence) - 1]
        if not left or not right:
            return True
        return self.VerifySquenceOfBST(left) and self.VerifySquenceOfBST(right)

if __name__ == '__main__':
    print Solution().VerifySquenceOfBST([1, 2, 3, 4, 5])