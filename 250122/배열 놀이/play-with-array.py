n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(arr[a[1]-1])
    elif a[0] == 2:
        for j in range(n):
            if arr[j] == a[1]:
                print(j+1)
                break
        else:
            print(0)
    elif a[0] == 3:
        start, end = a[1] - 1, a[2]
        print(" ".join(map(str, arr[start:end])))