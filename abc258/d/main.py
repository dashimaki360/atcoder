#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**20

n,x = LI()
c = 0

ans = math.inf
for i in range(n):
    a, b = LI()
    c += a+b
    if x-i-1 < 0: break
    tmp = c + b*(x-i-1)
    ans = min(ans, tmp)
print(ans)


