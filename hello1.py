# -*- coding:utf-8 -*-
from __future__ import division
if __name__ == '__main__':
    # 输入n
    n = int(raw_input())
    # 定义保存斜率的字典map
    kmap = {}
    people = 2  # hr看到的人数
    # 从下往上一层一层遍历结点，斜率没有出现在字典中结点是hr可以看到的，如果当前斜率出现过，说明他被遮挡遮住了，hr看到的人数不会增加
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            k = j / i
            if k not in kmap:
                kmap[k] = 1
                people += 1
    # 打印hr看到的人数
    print people
    # 初步代码









