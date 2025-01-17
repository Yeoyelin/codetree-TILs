result = list(map(int, input().split()))
cnt = [0]*7

for elem in result:
    cnt[elem] += 1
for i in range(1, 7):
    num = cnt[i]
    print("%d - %d"%(i, num))