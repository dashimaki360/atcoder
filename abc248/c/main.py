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

n,m,k = LI()

dp = [[0]*3000 for _ in range(55)]
dp[0][0] = 1
for i in range(n):
    for j in range(k+1):
        for l in range(1,m+1):
            if j+l > k: continue
            dp[i+1][j+l] += dp[i][j]
            dp[i+1][j+l] %= MOD
ans = sum(dp[n])
ans %= MOD
print(ans)

