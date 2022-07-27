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
H = 5005
P = [[0]*(H) for _ in range(H)]
for _ in range(n):
    a,b = LI()
    P[a][b] += 1

for i in range(H):
    for j in range(1,H):
        P[i][j] = P[i][j-1] + P[i][j]
for j in range(H):
    for i in range(1,H):
        P[i][j] = P[i-1][j] + P[i][j]


ans = 0
k += 1
for i in range(H-k):
    for j in range(H-k):
        tmp = P[i+k][j+k] - P[i][j+k] - P[i+k][j] + P[i][j]
        ans = max(ans,tmp)
print(ans)
