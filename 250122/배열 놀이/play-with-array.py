n, q = input().split()
arr = list(map(int, input().split()))

for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(arr[a[1]-1])
    elif a[0] == 2:
        for j in range(n):
            if arr[j] == a[1]:
                print(len(arr[j]))
                break
        else:
            print(0)
    else:
        for j in range(a[1]-1, a[2]):
            print(arr[j], end = " ")