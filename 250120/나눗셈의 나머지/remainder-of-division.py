a, b = map(int, input().split())
nam = [0]*b

while a>1:
    c = a%b
    nam[c] += 1
    a = a//b

ans = 0
for i in nam:
    double = i*i
    ans += double

print(ans)