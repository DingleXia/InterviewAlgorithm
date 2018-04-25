# -*- coding:utf-8 -*-
import itertools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        strNum = [str(_) for _ in numbers]
        strPer = map(''.join, list(itertools.permutations(strNum)))
        nums = [int(_) for _ in strPer]
        return min(nums)

if __name__ == '__main__':
    print Solution().PrintMinNumber([3, 32, 321])

# -*- coding:utf-8 -*-
# class Solution:
#     def PrintMinNumber(self, numbers):
#         # write code here
#         if not numbers:
#             return ""
#         lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
#         array = sorted(numbers, cmp=lmb)
#         return ''.join([str(i) for i in array])


