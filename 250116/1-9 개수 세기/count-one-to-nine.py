n = int(input())
count_arr = [0] * 10

arr = list(map(int, input().split()))
for elem in arr:
    count_arr[elem] += 1
for i in range(1, 10):
    cnt = count_arr[i]
    if cnt>0:
        print(cnt)
    else:
        print(0)