# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        newStr = ""
        for c in s:
            if c == ' ':
                newStr += '%20'
            else:
                newStr += c
        return newStr

if __name__ == '__main__':
    print Solution().replaceSpace('We are happy')