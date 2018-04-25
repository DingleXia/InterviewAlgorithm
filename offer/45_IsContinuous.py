# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        nums = sorted(numbers)
        i = 0
        zeros = 0
        while nums[i] == 0:
            zeros += 1
            i += 1
        if zeros >= 4:
            return 'Error'
        if i == len(nums):
            return True
        while i < len(nums) - 1:
            gap = nums[i + 1] - nums[i] - 1
            if gap < 0:
                return False
            if gap > zeros:
                return False
            else:
                zeros -= gap
            i += 1
        return True

if __name__ == '__main__':
    print Solution().IsContinuous([1, 3, 4, 0, 5])
    print Solution().IsContinuous([1, 3, 4, 0, 6])
