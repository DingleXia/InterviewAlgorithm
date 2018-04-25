# -*- coding:utf-8 -*-
# 给出一个不需要自己输入数据的案例
# 下个文件需要自己手动输入数据
if __name__ == '__main__':
    # 这一题我用map来改进，只要遍历完所有数组，用map把数和数出现的次数保存起来，key是数，value是出现的次数
    # 有序数组个数
    m = 3
    # 有序数组
    array = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    # 数字出现最少次数
    n = 2
    # 用map统计所有数字出现的次数
    d = {}
    for a in array:
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    # 保存次数大于n次的结果
    res = []
    for k in d:
        if d[k] >= 2:
            res.append(k)
    print res   # 打印结果

