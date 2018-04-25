# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        r = ""
        i = 0
        start = 0
        count = 0
        while i < len(s):
            while i < len(s) and s[i] is not ' ':
                count += 1
                i += 1
            r += s[start:start + count][::-1]
            while i < len(s) and s[i] is ' ':
                r += ' '
                i += 1
            start = i
            count = 0
        return r[::-1]

if __name__ == '__main__':
    print Solution().ReverseSentence("I am a student.")
