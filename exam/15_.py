# -*- coding:utf-8 -*-
"""
题目描述
考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法： 1.根据字符串的字典序排序。例如：
"car" < "carriage" < "cats" < "doggies < "koala"
2.根据字符串的长度排序。例如：
"car" < "cats" < "koala" < "doggies" < "carriage"
考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。
输入描述:

输入第一行为字符串个数n(n ≤ 100)
接下来的n行,每行一个字符串,字符串长度均小于100，均由小写字母组成

输出描述:

如果这些字符串是根据字典序排列而不是根据长度排列输出"lexicographically",

如果根据长度排列而不是字典序排列输出"lengths",

如果两种方式都符合输出"both"，否则输出"none"

示例1
输入

3
a
aa
bbb

输出

both
"""
def isDictionaryOrder(array):
    def cmp(s1, s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] > s2[i]:
                return False
            elif s1[i] < s2[i]:
                return True
            else:
                i += 1
        if i == len(s1):
            return True
        else:
            return False
    i = 0
    while i < len(array) - 1:
        if cmp(array[i], array[i + 1]):
            i += 1
        else:
            return False
    return True

def isQuantityOrder(array):
    quantity = [len(a) for a in array]
    i = 0
    while i < len(quantity) - 1:
        if quantity[i] < quantity[i + 1]:
            i += 1
        else:
            return False
    return True


if __name__ == '__main__':
    n = int(raw_input())
    array = []
    for i in range(n):
        array.append(raw_input())
    # print n
    # print array
    if isDictionaryOrder(array) and not isQuantityOrder(array):
        print 'lexicographically'
    elif not isDictionaryOrder(array) and isQuantityOrder(array):
        print 'lengths'
    elif isDictionaryOrder(array) and isQuantityOrder(array):
        print 'both'
    else:
        print 'none'

