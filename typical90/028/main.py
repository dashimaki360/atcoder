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
A = [[0]*1005 for _ in range(1005)]
for _ in range(n):
    x1, y1, x2, y2 = LI()
    A[x1][y1] += 1
    A[x1][y2] -= 1
    A[x2][y1] -= 1
    A[x2][y2] += 1

for i in range(1005):
    for j in range(1,1005):
        A[i][j] = A[i][j-1]+A[i][j]

for i in range(1005):
    for j in range(1,1005):
        A[j][i] = A[j-1][i]+A[j][i]

ans = [0]*(n+1)
for i in range(1005):
    for j in range(1005):
        ans[A[i][j]] += 1

for i in range(1,n+1):
    print(ans[i])