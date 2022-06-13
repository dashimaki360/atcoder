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

n,m = LI()
s = LI()
x = LI()
dp = [[1]*m for _ in range(n)]

for i in range(1,n):
    for j in range(m):
        if i >= 3:
            dp[i][j] = max(dp[i-3])
        for k in range(m):
            if i >= 2:
                if s[i-2] - x[k] + x[j] == s[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-2][k]+1)
            if s[i-1] == x[k]+x[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][k]+1)
    # print(dp[i])

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])
print(ans)

