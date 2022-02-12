#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(b) - max(a) + 1
ans = max(ans, 0)

print(ans)