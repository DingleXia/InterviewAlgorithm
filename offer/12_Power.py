# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent < 0:
            return 'Error'
        if exponent == 0:
            return 1
        if base == 0 and exponent > 0:
            return 0
        if exponent < 0:
            return 1.0 / self.Power(base, -exponent)
        result = self.Power(base, exponent / 2) ** 2
        if exponent & 1:
            return base * result
        else:
            return result

if __name__ == '__main__':
    print Solution().Power(2, 3)
