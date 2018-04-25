# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        def nOf1(q):
            index = 0
            for i in str(q):
                if i == '1':
                    index += 1
            return index
        sum = 0
        for q in range(1, n + 1):
            sum += nOf1(q)

        return sum

if __name__ == '__main__':
    print Solution().NumberOf1Between1AndN_Solution(9)

# -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1Between1AndN_Solution(self, n):
#         # write code here
#         res=0
#         tmp=n
#         base=1
#         while tmp:
#             last=tmp%10
#             tmp=tmp/10
#             res+=tmp*base
#             if last==1:
#                 res+=n%base+1
#             elif last>1:
#                 res+=base
#             base*=10
#         return res
