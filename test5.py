def getByI(i, num):
    if i == 1:
        return num
    else:
        return (num - 10 ** (i - 1) + 1) * i * getByI(i - 1, num)


def numOfW(num):
    i = 0
    a = num
    while a:
        a = a / 10
        i += 1
    return getByI(i, num)



n = int(raw_input())
i = 0
while i < n:
    num = int(raw_input())
    print numOfW(num)


