# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        n = sorted(numbers)
        l = 0
        index = 0
        for i in range(len(n)):
            if n[i] == n[index]:
                i += 1
                if i - index > len(n) / 2:
                    return n[index]
            else:
                index = i
        return 0

if __name__ == '__main__':
    print Solution().MoreThanHalfNum_Solution([3, 2, 2, 2, 1])

# import collections
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         tmp = collections.Counter(numbers)
#         x = len(numbers)/2
#         for k, v in tmp.items():
#             if v > x:
#                 return k
#         return 0
