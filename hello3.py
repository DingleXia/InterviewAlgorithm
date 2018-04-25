# -*- coding:utf-8 -*-
if __name__ == '__main__':
    # 这一题我用map来改进，只要遍历完所有数组，用map把数和数出现的次数保存起来，key是数，value是出现的次数
    m = int(raw_input())     # 有序数组个数
    # 有序数组
    array = []
    for i in range(m):
        array.append([int(_) for _ in raw_input().split(' ')])
    # print m
    # print array
    # 数字出现最少次数
    n = int(raw_input())
    # print n
    # 用map统计所有数字出现的次数
    d = {}
    for a in array:
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    # print d
    # 保存次数大于n次的结果
    res = []
    for k in d:
        if d[k] >= 2:
            res.append(k)
    print res   # 打印结果
