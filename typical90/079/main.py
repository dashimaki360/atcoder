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
B = []
for _ in range(h):
    A.append(LI())
for _ in range(h):
    B.append(LI())

for i in range(h):
    for j in range(w):
        A[i][j] -= B[i][j]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        x = A[i][j]
        A[i][j] -= x
        A[i+1][j] -= x
        A[i][j+1] -= x
        A[i+1][j+1] -= x
        ans += abs(x)

for i in range(h):
    for j in range(w):
        if A[i][j] != 0:
            no()
            exit()
else:
    yes()
    print(ans)