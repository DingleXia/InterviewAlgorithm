# -*- coding:utf-8 -*-
"""
题目描述
你就是一个画家！你现在想绘制一幅画，但是你现在没有足够颜色的颜料。为了让问题简单，我们用正整数表示不同颜色的颜料。你知道这幅画需要的n种颜色的颜料，你现在可以去商店购买一些颜料，但是商店不能保证能供应所有颜色的颜料，所以你需要自己混合一些颜料。混合两种不一样的颜色A和颜色B颜料可以产生(A XOR B)这种颜色的颜料(新产生的颜料也可以用作继续混合产生新的颜色,XOR表示异或操作)。本着勤俭节约的精神，你想购买更少的颜料就满足要求，所以兼职程序员的你需要编程来计算出最少需要购买几种颜色的颜料？
输入描述:

第一行为绘制这幅画需要的颜色种数n (1 ≤ n ≤ 50)
第二行为n个数xi(1 ≤ xi ≤ 1,000,000,000)，表示需要的各种颜料.

输出描述:

输出最少需要在商店购买的颜料颜色种数，注意可能购买的颜色不一定会使用在画中，只是为了产生新的颜色。

示例1
输入

3
1 7 3

输出

3

"""
def binaryLength(num):
    len = 0
    while num:
        len += 1
        num >>= 1
    return len
if __name__ == '__main__':
    n = int(raw_input())
    nums = map(int, raw_input().split())
    # n = 3
    # nums = [1, 7, 3]
    # n = 15
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(n):
        nums[i:] = sorted(nums[i:], reverse=True)
        iLen = binaryLength(nums[i])
        for j in range(i + 1, n):
            jLen = binaryLength(nums[j])
            if iLen == jLen:
                nums[j] = nums[i] ^ nums[j]
    print len([x for x in nums if x != 0])


