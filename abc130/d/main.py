#!/usr/bin/env python3
import sys
from collections import deque
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

n, k = LI()
A = LI()

ans = 0
r = 0
p = A[0]
for l in range(n):
    while r < n-1 and p < k:
        r += 1
        p += A[r]
    if p < k:
        break
    ans += n - r
    p -= A[l]

print(ans)

