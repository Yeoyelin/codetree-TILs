num = list(map(int, input().split()))

tens= [x // 10 for x in num]

count = [0]*10
for elem in tens:
    if 0<elem:
        count[elem] += 1
    else:
        count[elem] += 0
for i in range(1, 10):
    print("%d - %d"%(i, count[i]))
