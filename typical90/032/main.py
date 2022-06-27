#!/usr/bin/env python3
import itertools
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
A = []
for _ in range(n):
    A.append(LI())
m = I()
bad = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = LI()
    bad[a-1][b-1] = 1
    bad[b-1][a-1] = 1

import itertools
it = itertools.permutations(range(n),n)
ans = INF
for p in it:
    time = 0
    for i in range(n):
        if i+1 < n and bad[p[i]][p[i+1]]:
            break
        time += A[p[i]][i]
    else:
        ans = min(ans, time)

if ans == INF:
    ans = -1
print(ans)
