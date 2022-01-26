import math

n = int(input())
xs = []
ys = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    xs.append(a)
    ys.append(b)

for i in range(n):
    for j in range(n):
        ans = max(math.sqrt((xs[i]-xs[j])**2 + (ys[i] - ys[j])**2), ans)

print(ans)
