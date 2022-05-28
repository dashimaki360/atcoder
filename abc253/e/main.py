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

n, m, k= LI()

dp = [[0]*5005 for _ in range(1005)]
for j in range(1,m+1):
    dp[1][j] = dp[1][j-1] + 1

for i in range(2,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][m]
        if k > 0:
            dp[i][j] -= dp[i-1][min(m,j+k-1)] - dp[i-1][max(0,j-k)]
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD

ans = dp[n][m] % MOD
print(ans)



