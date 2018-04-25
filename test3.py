import math
while 1:
    array = map(int, raw_input().split())
    num, k = array[0], array[1]
    if num < 0:
        print num
    else:
        tmp, total = num, num
        for i in range(k - 1):
            tmp = math.sqrt(tmp)
            total += tmp
        print float('%.2f' % total)





