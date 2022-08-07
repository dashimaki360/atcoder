#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n = I()
A = LI()

def solve(x):
    dp = [[0]*x for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        a = A[i]
        for j in range(i,-1,-1):
            for k in range(x):
                dp[j+1][(k+a)%x] += dp[j][k]
                dp[j+1][(k+a)%x] %= MOD
        # print(dp)

    return dp[x][0]
ans = 0

for i in range(1,n+1):
    ans += solve(i)
    ans %= MOD
    
print(ans)
