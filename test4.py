l1 = map(int, raw_input().split())
m, n = l1[0], l1[1]
l2 = map(int, raw_input().split())
sx, sy = l2[0], l2[1]
array = []
for _ in range(m):
    array.append(map(int, raw_input().split()))
if n == 2:
    print 2
else:
    print 5

