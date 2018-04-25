# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        if not s[0].isdigit() and s[0] is not '+' and s[0] is not '-':
            return 0
        if s[0] is '+' and len(s) == 1 or s[0] is '-' and len(s) == 1:
            return 0
        for i in range(1, len(s)):
            if not s[i].isdigit():
                return 0
        if s[0] == '-':
            return -int(s[1:])
        elif s[0] == '+':
            return int(s[1:])
        else:
            return int(s)

if __name__ == '__main__':
    print Solution().StrToInt('+123')
    print Solution().StrToInt('-123')
    print Solution().StrToInt('1a2')
