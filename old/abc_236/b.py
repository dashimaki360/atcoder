import math

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += 4*(i+1)

for aa in a:
    ans -= aa

print(ans)
