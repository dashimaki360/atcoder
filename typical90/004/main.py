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

h,w = LI()
A = []
for _ in range(h):
    A.append(LI())

sumh = [0]*h
sumw = [0]*w
for i in range(h):
    sumh[i] = sum(A[i])
for i in range(w):
    for j in range(h):
        sumw[i] += A[j][i]
ans = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = sumh[i]+sumw[j] - A[i][j]

for an in ans:
    print(*an)


