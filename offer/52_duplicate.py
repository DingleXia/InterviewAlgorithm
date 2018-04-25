# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        nums = sorted(numbers)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                duplication[0] = nums[i]
                return True
            i += 1
        return False

if __name__ == '__main__':
    numbers = [2, 3, 1, 0, 2, 5, 3]
    duplication = [0]
    print Solution().duplicate(numbers, duplication)
    print duplication
