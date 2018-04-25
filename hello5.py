# -*- coding:utf-8 -*-
# 改进版本利用二分查找，首先获取m数组中的最大值，最小值，在最大最小值之间的所有数在数组中二分查找
if __name__ == '__main__':
    # 二分查找，在数组中找到返回True, 没找到返回false
    def binary_search(array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if array[mid] > target:
                right = mid - 1
            elif array[mid] < target:
                    left = mid + 1
            else:
                return True
        return False
    # 测试binary_search的正确性
    # print binary_search([1, 2, 3, 4, 5], 0)
    # print binary_search([1, 2, 3, 4, 5], 6)
    # print binary_search([1, 2, 3, 4, 5], 4)

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

    # 获取m个数组的最大值，最小值，因为数组有序所以时间复杂度O(m)
    minNum, maxNum = float("inf"), float("-inf")
    for a in array:
        if array:
            minNum = min(minNum, a[0])
            maxNum = max(maxNum, a[-1])
    # print minNum, maxNum
    # 从最小到最大值到在m个数组中进行二分查找，时间复杂度O((maxNum - minNum) * m * logn),n为每个数组元素个数
    d = {}
    for i in range(minNum, maxNum + 1):
        for a in array:
            if binary_search(a, i):
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
    # print d
    # 保存次数大于n次的结果
    res = []
    for k in d:
        if d[k] >= 2:
            res.append(k)
    print res  # 打印结果

    # 算法中时间复杂度为 O(m) + O((maxNum - minNum) * m * logn)
    # 若maxNum - minNum 差距不太大， 例如最小的数是1， 最大的数是100，那么算法的时间复杂度近似为
    #O(m * logn) 此时的算法比之前的算法O(m * n)要好很多



