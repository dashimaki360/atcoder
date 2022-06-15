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
A = LI()
n2 = 2*n

dp = [[INF]*405 for _ in range(405)]

for i in range(n2-1):
    dp[i][i+2] = abs(A[i] - A[i+1])

for w in range(4,n2+1,2):
    for l in range(n2):
        r = l+w
        if r > n2: continue
        for k in range(2,w,2):
            dp[l][r] = min(dp[l][r], dp[l][l+k]+dp[l+k][r])
        dp[l][r] = min(dp[l][r], dp[l+1][r-1]+abs(A[l]-A[r-1]))
ans = dp[0][n2]
print(ans)


