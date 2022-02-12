#!/usr/bin/env python3
n, k = map(int, input().split())
for _ in range(k):
    if n % 200 == 0:
        n = n//200
    else:
        n = n*1000 + 200
print(n)
