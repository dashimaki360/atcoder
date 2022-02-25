#!/usr/bin/env python3
n,k = map(int, input().split())
ans = 0
for i in range(1,n+1):
  for j in range(1001001001):
    if i*(2**j) >= k:
      ans += 0.5**j
      break
ans = ans/n
print(ans)
