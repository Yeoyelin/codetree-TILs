num = list(map(int, input().split()))
if 0 in num:
    num = num[:num.index(0)]
    
tens= [x // 10 for x in num]

count = [0]*10
for elem in tens:
    if 0<=elem<10:
        count[elem] += 1
for i in range(1, 10):
    print("%d - %d"%(i, count[i]))