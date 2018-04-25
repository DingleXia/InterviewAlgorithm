# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.buffer = ''
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        appear = [False for _ in range(256)]
        for b in self.buffer:
            if appear[ord(b)] is False:
                appear[ord(b)] = True
            else:
                appear[ord(b)] = False
        for b in self.buffer:
            if appear[ord(b)] is True:
                return b
        return '#'

    def Insert(self, char):
        # write code here
        self.buffer += char

if __name__ == '__main__':
    s = Solution()
    s.Insert('google')
    print s.FirstAppearingOnce()
