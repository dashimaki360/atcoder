#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

l1,r1,l2,r2 = LI()
ans = 0
for i in range(200):
    if l1 <= i <= r1 and l2 <= i <= r2:
        ans += 1
ans = max(0,ans-1)
print(ans)
