#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n,k = LI()
A = LI()
P = []
for _ in range(n):
    x,y = LI()
    P.append([x,y])

ans = 0
for i in range(n):
    mind = INF
    for a in A:
        a -= 1
        x = (P[i][0]- P[a][0])**2 + (P[i][1]-P[a][1])**2
        x = x**0.5
        mind = min(mind,x)
    ans = max(ans,mind)
print(ans)

