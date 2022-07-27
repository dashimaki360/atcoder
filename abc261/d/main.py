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

n,m = LI()
X = LI()
Y = [0]*5005
for i in range(m):
    c,y = LI()
    Y[c] = y

dp = [[-1]*5005 for _ in range(5005)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:continue
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + Y[j+1])
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])

ans = max(dp[n])
print(ans)
