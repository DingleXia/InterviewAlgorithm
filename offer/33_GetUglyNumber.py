# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        UglyNum = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0
        for i in range(index - 1):
            NewUgly = min(UglyNum[indexTwo] * 2, UglyNum[indexThree] * 3, UglyNum[indexFive] * 5)
            UglyNum.append(NewUgly)
            if NewUgly % 2 == 0:
                indexTwo += 1
            if NewUgly % 3 == 0:
                indexThree += 1
            if NewUgly % 5 == 0:
                indexFive += 1
        return UglyNum[-1]

if __name__ == '__main__':
    print Solution().GetUglyNumber_Solution(1)
    print Solution().GetUglyNumber_Solution(2)
    print Solution().GetUglyNumber_Solution(3)
    print Solution().GetUglyNumber_Solution(4)
    print Solution().GetUglyNumber_Solution(5)
    print Solution().GetUglyNumber_Solution(6)
    print Solution().GetUglyNumber_Solution(7)
    print Solution().GetUglyNumber_Solution(8)
