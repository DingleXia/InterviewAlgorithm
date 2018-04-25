# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n <= 0:
            return s
        if not s:
            return ""
        n = n % len(s)
        a = s[:n][::-1]
        b = s[n:][::-1]
        return (a + b)[::-1]

if __name__ == '__main__':
    print Solution().LeftRotateString("abcdefg", 2)
