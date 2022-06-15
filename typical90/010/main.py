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
P = [[0]*n for _ in range(2)]
sumP = [[0]*(n+1) for _ in range(2)]
for i in range(n):
    c,p = LI()
    P[c-1][i] = p
for c in range(2):
    for i in range(n):
        sumP[c][i+1] = sumP[c][i] + P[c][i]

q = I()
for _ in range(q):
    l,r = LI()
    ans = [0]*2
    for c in range(2):
        ans[c] = sumP[c][r] - sumP[c][l-1]
    print(*ans)
        


