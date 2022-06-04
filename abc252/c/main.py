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

n = I()
s = [S() for _ in range(n)]

ans = INF
for i in range(10):
    p = [-1 for j in range(10)]
    for j in range(n):
        for k in range(10):
            if int(s[j][k]) == i:
                if p[k] == -1:
                    p[k] = k
                else:
                    p[k] += 10
    ans = min(ans, max(p))
print(ans)
            
            
            