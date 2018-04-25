# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0])
        brow, bcol = 0, 0
        erow, ecol = rows - 1, cols - 1
        index = 0
        m = []
        while brow <= erow and bcol <= ecol:
            if index % 4 == 0:
                for i in range(bcol, ecol + 1):
                    m.append(matrix[brow][i])
                brow += 1
                index += 1
            elif index % 4 == 1:
                for i in range(brow, erow + 1):
                    m.append(matrix[i][ecol])
                ecol -= 1
                index += 1
            elif index % 4 == 2:
                for i in range(ecol, bcol - 1, -1):
                    m.append(matrix[erow][i])
                erow -= 1
                index += 1
            else:
                for i in range(erow, brow - 1, -1):
                    m.append(matrix[i][bcol])
                bcol += 1
                index += 1
        return m

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print Solution().printMatrix(matrix)
