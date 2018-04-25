# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False

if __name__ == '__main__':
    print Solution().isNumeric('+12e4.3')
    print Solution().isNumeric('+-5')
    print Solution().isNumeric('+1e5')
    print Solution().isNumeric('-3.14152')
    print Solution().isNumeric('1a2')
