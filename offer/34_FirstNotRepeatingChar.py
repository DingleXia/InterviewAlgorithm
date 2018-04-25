# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i

if __name__ == '__main__':
    print Solution().FirstNotRepeatingChar('abcab')
