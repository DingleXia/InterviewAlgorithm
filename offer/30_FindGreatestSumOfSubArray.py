# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        all = [array[:i + 1] for i in range(len(array))]
        allSum = map(sum, all)
        max = float('-inf')
        for i in range(len(allSum)):
            for j in range(i + 1, len(allSum)):
                if allSum[j] - allSum[i] > max:
                    max = allSum[j] - allSum[i]
        if allSum[-1] > max:
            max = allSum[-1]
        return max

if __name__ == '__main__':
    print Solution().FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2])

# -*- coding:utf-8 -*-
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         # write code here
#         max_sum, cur_sum = -0xffffff, 0
#         for i in array:
#             if cur_sum <= 0:
#                 cur_sum = i
#             else:
#                 cur_sum += i
#             if cur_sum > max_sum:
#                 max_sum = cur_sum
#         return max_sum
